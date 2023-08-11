"""
_summary_ my code
"""
import requests
"""
_summary_ my code
"""
url= "https://alu-intranet.hbtn.io/status"
"""
    commit my code
"""
response = requests.get(url)
"""commented
"""
if response.status_code == 200:
    """
    commit my code
    """
    content = response.json()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
else:
    print(f"Request failed with status code: {response.status_code}")