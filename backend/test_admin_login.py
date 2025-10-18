import requests

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

def test_admin_login():
    """Test admin login with correct credentials"""
    print("Testing admin login with correct credentials...")
    
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
        
        if response.status_code == 200:
            print("Admin login successful!")
            print(f"Response data: {response.json()}")
        else:
            print(f"Error response: {response.text}")
        return response
    except Exception as e:
        print(f"Error during admin login: {e}")
        return None

def test_admin_login_incorrect():
    """Test admin login with incorrect credentials"""
    print("\nTesting admin login with incorrect credentials...")
    
    login_data = {
        "username": "wronguser",
        "password": "wrongpass"
    }
    
    try:
        # Need to send as form data for OAuth2
        response = requests.post(
            f"{BASE_URL}/auth/login", 
            data=login_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        print(f"Incorrect admin login response: {response.status_code}")
        
        if response.status_code == 401:
            print("Correctly rejected incorrect credentials")
        else:
            print(f"Unexpected response: {response.text}")
        return response
    except Exception as e:
        print(f"Error during incorrect admin login: {e}")
        return None

if __name__ == "__main__":
    test_admin_login()
    test_admin_login_incorrect()