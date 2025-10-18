import requests
import json

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

def test_user_registration():
    """Test user registration"""
    print("Testing user registration...")
    
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
        print(f"Registration response: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print(f"Response data: {response.json()}")
        else:
            print(f"Error response: {response.text}")
        return response
    except Exception as e:
        print(f"Error during registration: {e}")
        return None

if __name__ == "__main__":
    test_user_registration()