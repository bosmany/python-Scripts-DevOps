# Script: Make HTTP Requests to APIs
 # Install requests first:
 # pip install requests
==========================================
import requests

def call_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        print("API Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")

# Example usage
call_api("https://jsonplaceholder.typicode.com/posts/1")

