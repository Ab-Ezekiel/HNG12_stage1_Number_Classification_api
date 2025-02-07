# HNG12_stage1_Number_Classification_api
HNG12 stage1: Number classification api

This API classifies a given number based on mathematical properties such as primality, Armstrong status, and parity. It also fetches an interesting fact about the number using the Numbers API.
Features

    Checks if a number is prime
    Determines if a number is an Armstrong number
    Identifies if a number is odd or even
    Computes the sum of digits
    Fetches a fun fact about the number

API Endpoint
GET /api/classify-number?number=<integer>
Example Request:

curl -X GET "https://your-deployment-url.com/api/classify-number?number=371"

Example Response:

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Handling

If a non-integer input is provided, the API returns:

{
    "number": "invalid_input",
    "error": true
}

Deployment URL

🔗 Live API: https://your-deployment-url.com
Installation & Setup

    Clone the Repository

git clone https://github.com/Ab-Ezekiel/HNG12_stage1_Number_Classification_api.git
cd HNG12_stage1_Number_Classification_api

Create a Virtual Environment & Install Dependencies

python3 -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
pip install -r requirements.txt

Run the API Locally

    python app.py

    The API will be available at: http://127.0.0.1:5000

Deployment

This API is deployed on Render. The start command used:

gunicorn wsgi:app

Technologies Used

    Python (Flask) – Web framework
    Gunicorn – WSGI server for production
    Requests – Fetching external API data
    Flask-CORS – Handling cross-origin requests


