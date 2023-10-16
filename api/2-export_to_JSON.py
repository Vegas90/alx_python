import json
import requests
import sys
# Get the employee ID from the command line
employee_id = int(sys.argv[1])
# Get the employee's TODO list
response = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
todos = response.json()
# Get the employee's name
response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
employee = response.json()
employee_name = employee["name"]
# Create a dictionary to store the data
data = {}
data[employee_id] = []
# Add the tasks to the dictionary
for todo in todos:
    data[employee_id].append({"task": todo["title"], "completed": todo["completed"], "username": employee_name})
# Write the data to a JSON file
with open("{}.json".format(employee_id), "w") as jsonfile:
    json.dump(data, jsonfile)