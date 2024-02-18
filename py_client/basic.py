import requests

endpoint = 'http://127.0.0.1:8000/api/'

# Sending parameters through the URL query string and JSON payload in the request body
get_response = requests.get(endpoint, params={"abc": 1234}, json={"query": "Hello world"})

# Printing the JSON response
print(get_response.json())