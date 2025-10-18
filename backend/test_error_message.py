import requests

# Base URL for the backend API
BASE_URL = "http://localhost:8001/api"

def test_error_message():
    """Test that error message is generic and doesn't reveal credential information"""
    print("Testing error message for incorrect admin credentials...")
    
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
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        
        # Check that the error message is generic
        if response.status_code == 401:
            if "Invalid credentials" in response.text:
                print("✓ Error message is generic and doesn't reveal credential information")
            else:
                print("✗ Error message may reveal too much information")
        else:
            print(f"Unexpected response status: {response.status_code}")
        return response
    except Exception as e:
        print(f"Error during test: {e}")
        return None

if __name__ == "__main__":
    test_error_message()