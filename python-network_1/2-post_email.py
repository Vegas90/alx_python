import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

response= requests.post(url, data=email)
print(f"Email: {email}")
