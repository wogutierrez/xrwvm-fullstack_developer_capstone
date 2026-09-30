# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url',
    default="http://localhost:3030"
)
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """Send GET request to backend."""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params
    print(f"GET from {request_url}")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")


def analyze_review_sentiments(text):
    """Send text to sentiment analyzer service."""
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected error: {err}, type: {type(err)}")
        print("Network exception occurred")


def post_review(data_dict):
    """Post review data to backend."""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
