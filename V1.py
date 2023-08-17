 import requests

def is_valid_url(url):
    # Implement your URL validation logic here
    # Return True if the URL is valid, False otherwise
    pass

def make_request(url):
    if is_valid_url(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except requests.RequestException as e:
            return f"Request Error: {e}"
    else:
        return "Invalid URL"

if __name__ == "__main__":
    user_input = input("Enter a URL: ")
    result = make_request(user_input)
    print(result)
