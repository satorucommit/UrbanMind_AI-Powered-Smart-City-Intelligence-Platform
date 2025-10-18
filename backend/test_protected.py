import requests
import json

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

def test_protected_endpoint(token):
    """Test accessing protected endpoint"""
    print("Testing protected endpoint...")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/protected/protected", headers=headers)
    print(f"Protected endpoint response: {response.status_code}")
    print(f"Response headers: {response.headers}")
    print(f"Response text: {response.text}")
    
    if response.status_code == 200:
        print(f"Response data: {response.json()}")
    else:
        print(f"Error response: {response.text}")
    
    return response

if __name__ == "__main__":
    # Use the token from the previous test
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsInJvbGUiOiJ1c2VyIiwiZXhwIjoxNzYwNzIwNjY4fQ.4WVwk_oGgT5ELSAF3iV8xeKWehZoeEjaeMsH_FcnlPQ"
    test_protected_endpoint(token)