import requests
from exceptions import RequestTimeoutError, RequestError

def make_request(url):
    try:
        response = requests.get(url, timeout=5)  # Add a timeout for the request
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.text
    except requests.exceptions.Timeout:
        raise RequestTimeoutError("Request Timed Out")
    except requests.exceptions.RequestException as e:
        raise RequestError(f"Request Error: {e}")
