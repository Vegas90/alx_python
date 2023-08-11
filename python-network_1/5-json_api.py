import requests
import sys

url= "http://0.0.0.0:5000/search_user"

if len(sys.argv) > 1:
    q = sys.argv[1]
response = requests.get(url)
try:
    colar= response.json()
    if colar is not None:
        print('[', colar['id'], '] ', colar['name'])
    else:
        print("No result")
    
except ValueError:
    print("Not a valid JSON")



