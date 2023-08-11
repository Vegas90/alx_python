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
print("Body response:")
print("type:", type(response.text))
print("content:", response.text)
