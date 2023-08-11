"""_summary_
"""
import requests
"""_summary_
"""
url= "https://alu-intranet.hbtn.io/status"

"""_summary_
"""
response = requests.get(url)
content = response.json()
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
