import requests
import sys
username = sys.argv[1]
password = sys.argv[2]
#user_id = get_user_id(username, password)

url = f"https://api.github.com/users/{username}"
response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    user_data = response.json()
    print(user_data['id'])

    
    
