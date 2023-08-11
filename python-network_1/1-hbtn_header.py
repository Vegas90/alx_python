import requests
import sys
"""cont"""
url="https://intranet.hbtn.io"
"""cont"""
response = requests.get(url)
"""cont"""
content_type = response.headers.get('X-Request-Id')
"""cont"""
print(content_type)