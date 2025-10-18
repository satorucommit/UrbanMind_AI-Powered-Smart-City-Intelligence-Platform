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
    
    response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    print(f"Registration response: {response.status_code}")
    print(f"Response data: {response.json()}")
    
    return response

def test_admin_registration():
    """Test admin registration"""
    print("\nTesting admin registration...")
    
    admin_data = {
        "username": "testadmin",
        "email": "admin@example.com",
        "full_name": "Test Admin",
        "password": "adminpassword"
    }
    
    response = requests.post(f"{BASE_URL}/auth/register/admin", json=admin_data)
    print(f"Admin registration response: {response.status_code}")
    print(f"Response data: {response.json()}")
    
    return response

def test_user_login():
    """Test user login"""
    print("\nTesting user login...")
    
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    
    # Need to send as form data for OAuth2
    response = requests.post(
        f"{BASE_URL}/auth/login", 
        data=login_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    print(f"Login response: {response.status_code}")
    print(f"Response data: {response.json()}")
    
    return response

def test_protected_endpoint(token):
    """Test accessing protected endpoint"""
    print("\nTesting protected endpoint...")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/protected/protected", headers=headers)
    print(f"Protected endpoint response: {response.status_code}")
    print(f"Response data: {response.json()}")
    
    return response

if __name__ == "__main__":
    print("Starting authentication tests...")
    
    # Test user registration
    reg_response = test_user_registration()
    
    # Test admin registration
    admin_reg_response = test_admin_registration()
    
    # Test user login
    login_response = test_user_login()
    
    if login_response.status_code == 200:
        token = login_response.json().get("access_token")
        # Test protected endpoint
        test_protected_endpoint(token)
    
    print("\nAuthentication tests completed.")