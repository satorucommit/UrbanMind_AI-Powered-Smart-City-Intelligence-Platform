import requests
import json

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

def test_user_login():
    """Test user login"""
    print("Testing user login...")
    
    login_data = {
        "username": "testuser",
        "password": "testpass"
    }
    
    try:
        # Need to send as form data for OAuth2
        response = requests.post(
            f"{BASE_URL}/auth/login", 
            data=login_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        print(f"Login response: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print(f"Response data: {response.json()}")
        else:
            print(f"Error response: {response.text}")
        return response
    except Exception as e:
        print(f"Error during login: {e}")
        return None

def test_admin_login():
    """Test admin login"""
    print("\nTesting admin login...")
    
    login_data = {
        "username": "admin",
        "password": "admin"
    }
    
    try:
        # Need to send as form data for OAuth2
        response = requests.post(
            f"{BASE_URL}/auth/login", 
            data=login_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        print(f"Admin login response: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            print(f"Response data: {response.json()}")
        else:
            print(f"Error response: {response.text}")
        return response
    except Exception as e:
        print(f"Error during admin login: {e}")
        return None

if __name__ == "__main__":
    test_user_login()
    test_admin_login()