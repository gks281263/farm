import requests
import json
import time
import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_tool.settings')

import django
django.setup()

BASE_URL = 'http://localhost:8000/api'

def test_jwt_authentication():
    """Test JWT authentication functionality"""
    print("\n=== Testing JWT Authentication ===")
    
    # Test credentials
        login_data = {
        'mobile_number': '9876543210',  # Using the superuser's mobile number
        'password': 'admin123'
        }
        
    try:
        # 1. Test Login
        print("\n1. Testing Login:")
        response = requests.post(f'{BASE_URL}/auth/login/', json=login_data)
        print(f"Status Code: {response.status_code}")
        print("Response:", json.dumps(response.json(), indent=2))
        
        if response.status_code != 200:
            print("❌ Login failed")
            return False
            
            tokens = response.json()
            access_token = tokens['access']
            refresh_token = tokens['refresh']
        print("✅ Login successful")
            
        # 2. Test Protected Endpoint Access
            headers = {'Authorization': f'Bearer {access_token}'}
        print("\n2. Testing Protected Endpoint Access:")
        
        # First try the profile endpoint
            profile_response = requests.get(f'{BASE_URL}/users/profile/', headers=headers)
        print(f"Profile Endpoint Status Code: {profile_response.status_code}")
        print("Profile Response:", json.dumps(profile_response.json(), indent=2))
        
        # If profile endpoint fails, try the users endpoint
        if profile_response.status_code != 200:
            print("\nTrying users endpoint instead...")
            users_response = requests.get(f'{BASE_URL}/users/', headers=headers)
            print(f"Users Endpoint Status Code: {users_response.status_code}")
            print("Users Response:", json.dumps(users_response.json(), indent=2))
            
            if users_response.status_code != 200:
                print("❌ Protected endpoint access failed")
                return False
        print("✅ Protected endpoint access successful")
            
            # 3. Test Token Refresh
        print("\n3. Testing Token Refresh:")
            refresh_data = {'refresh': refresh_token}
            refresh_response = requests.post(f'{BASE_URL}/token/refresh/', json=refresh_data)
            print(f"Status Code: {refresh_response.status_code}")
            print("Response:", json.dumps(refresh_response.json(), indent=2))
            
        if refresh_response.status_code != 200:
            print("❌ Token refresh failed")
            return False
        print("✅ Token refresh successful")
            
        # 4. Test Invalid Token
        print("\n4. Testing Invalid Token:")
            invalid_headers = {'Authorization': 'Bearer invalid_token'}
            invalid_response = requests.get(f'{BASE_URL}/users/profile/', headers=invalid_headers)
            print(f"Status Code: {invalid_response.status_code}")
            print("Response:", json.dumps(invalid_response.json(), indent=2))
            
        if invalid_response.status_code != 401:
            print("❌ Invalid token test failed")
            return False
        print("✅ Invalid token test successful")
        
        print("\n✅ All JWT authentication tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Error during JWT testing: {str(e)}")
        return False

def main():
    success = test_jwt_authentication()
    if not success:
        print("\n❌ JWT authentication tests failed")
        sys.exit(1)
    print("\n✅ JWT authentication is working properly!")

if __name__ == '__main__':
    main()