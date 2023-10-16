import csv
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
    user_id = employee_data['id']
    username = employee_data['username']

    # Retrieve employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Error: Could not fetch TODO list for ID {employee_id}")
        return

    todo_data = todo_response.json()

    # Calculate progress
    progress = []

    for task in todo_data:
        task_completed_status = "Completed" if task['completed'] else "Incomplete"
        task_title = task['title']
        progress.append([user_id, username, task_completed_status, task_title])

    # Export to CSV file
    csv_file_name = f"{user_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(progress)

    print(f"Employee {username} data has been exported to {csv_file_name}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
