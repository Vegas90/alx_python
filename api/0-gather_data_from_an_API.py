import requests
import sys

def get_employee_info(employee_id):
    # Retrieve employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Could not fetch employee details for ID {employee_id}")
        return

    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Retrieve employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for ID {employee_id}")
        return

    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")