import requests
import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def classify_name(request):
    name = request.query_params.get('name', 'all')
    if not name:
        return Response({"status": "error", "message": "Missing name"}, status=400)
    if not isinstance(name, str):
        return Response({"status": "error", "message": "Invalid name"}, status=422)

    try:
        target_url = f"https://api.genderize.io/?name={name}"
        response = requests.get(target_url)
        if response.status_code != 200:
            return Response({"status": "error", "message": "API error"}, status=502)
            
        data = response.json()
        gender = data.get("gender")
        probability = data.get("probability")
        count = data.get("count")
    
        if not gender or not probability or not count:
            return Response({"status": "error", "message": "No prediction available for the provided name"}, status=422)
    
        is_confident = probability >= 0.7 and count >= 100
        processed_at = datetime.datetime.utcnow().isoformat() + "Z"
    
        return Response({
            "status": "success",
            "data": {
                "name": name,
                "gender": gender,
                "probability": probability,
                "sample_size": count,
                "is_confident": is_confident,
                "processed_at": processed_at
            }
        }, status=200)
        
    except requests.exceptions.ConnectionError:
        return Response(
            {"status": "error", "message": "Could not connect to the service. Check the domain name or network."},
            status=503
        )
        
    except requests.exceptions.Timeout:
        return Response(
            {"status": "error", "message": "The request timed out."},
            status=504
        )
        
    except requests.exceptions.RequestException as e:
        return Response(
            {"status": "error", "message": f"An unexpected network error occurred: {str(e)}"},
            status=500
        )

    
