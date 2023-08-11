import requests
import sys

url= "http://0.0.0.0:5000/search_user"

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q=""
data = {'q': q}
    
response = requests.get(url, data=data)
try:
    colar= response.json()
    if colar is not None:
        print(f"[{colar['id']}] {colar['name']}")
    else:
        print("No result")
    
except ValueError:
    print("Not a valid JSON")

