# HNG Stage Zero: Name Classification API

This project provides a Django REST Framework API endpoint that classifies a given name by gender using the Genderize API.

## Features

*   **Gender Classification:** Takes a name as input and returns its predicted gender.
*   **Confidence Scoring:** Provides a confidence level for the prediction based on probability and sample size.
*   **API Integration:** Successfully integrates with the external Genderize API.
*   **Input Validation:** Robust validation for missing, empty, or non-string name inputs.
*   **Error Handling:** Gracefully handles API errors, connection issues, and timeouts.
*   **CORS Enabled:** Allows cross-origin requests, making it easy to integrate with frontend applications.
*   **Fast Response:** Optimized for quick responses, excluding external API latency.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/owoaanu/hng14_stage_zero.git
    cd hng14_stage_zero
    ```
2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` is not provided in the currently analyzed files, but this is a standard step.)*

4.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Endpoint

### `GET /api/classify`

This endpoint classifies a given name by gender.

**Query Parameters:**

*   `name` (string, **required**): The name to classify.

**Example Request:**

```bash
curl "http://127.0.0.1:8000/api/classify?name=Sammy"
```

**Successful Response (200 OK):**

```json
{
 "status": "success",
 "data": {
  "name": "Sammy",
  "gender": "male",
  "probability": 0.99,
  "sample_size": 1234,
  "is_confident": true,
  "processed_at": "2026-04-15T10:10:00Z"
 }
}
```

**Error Responses:**

*   **400 Bad Request (Missing or empty name):**
    ```json
    { "status": "error", "message": "Missing name" }
    ```
*   **422 Unprocessable Entity (Invalid name type or no prediction):**
    ```json
    { "status": "error", "message": "Invalid name" }
    ```
    or
    ```json
    { "status": "error", "message": "No prediction available for the provided name" }
    ```
*   **502 Bad Gateway (External API error):**
    ```json
    { "status": "error", "message": "API error" }
    ```
*   **503 Service Unavailable (Connection error to external API):**
    ```json
    { "status": "error", "message": "Could not connect to the service. Check the domain name or network." }
    ```
*   **504 Gateway Timeout (External API timeout):**
    ```json
    { "status": "error", "message": "The request timed out." }
    ```

**Notes on `settings.py`:**

*   `CORS_ALLOW_ALL_ORIGINS = True` is configured to allow all origins.


## Development

### Running the Server

```bash
python manage.py runserver
```

The server will typically start at `http://127.0.0.1:8000/`.

---

**Disclaimer:** This README is generated based on the provided `settings.py` and `views.py` files. Ensure all paths and details are accurate for your project setup.
