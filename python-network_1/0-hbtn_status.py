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
    #content = response.json()
    print("Body response:")
    print("type:", type(response))
    print("content:", response)
else:
    """
    commit 
    """
    print(f"Request failed with status code: {response.status_code}")