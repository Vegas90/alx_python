import requests
import sys

url = sys.argv[1]
response = requests.get(url)
"""cont"""
content_type = response.headers.get('X-Request-Id')
"""cont"""
print(content_type)