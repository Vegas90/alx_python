import requests
import sys
"""
    getting information of the url
"""
url=""
email=""
"""
    getting information of the url
"""
response = requests.post(url,data=email)
"""
    getting information of the url
"""
print(response.text)
