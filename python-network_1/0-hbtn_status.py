"""
importing
"""
import requests
"""
allocating url
"""
url= "https://alu-intranet.hbtn.io/status"
"""
    getting information of the url
"""
response = requests.get(url)
"""
commented
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
    """
    commit 
    """
    print(f"Request failed with status code: {response.status_code}")