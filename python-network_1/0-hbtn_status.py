"""_summary_"""
import requests
url= "https://alu-intranet.hbtn.io/status"

"""_summary_"""
response = requests.get(url)
""""summary"""
content = response.json()
""""summary"""
print("Body response:")
""""summary"""
print("\t- type:", type(content))
""""summary"""
print("\t- content:", content)
