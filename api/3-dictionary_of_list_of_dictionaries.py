import requests
import json

def get_all_employee_info():
    all_employee_data = {}

    # Retrieve all employee details
    employee_url = "https://jsonplaceholder.typicode.com/users"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Error: Could not fetch employee details.")
        return

    employee_data = employee_response.json()
    
    for employee in employee_data:
        user_id = employee['id']
        username = employee['username']

        # Retrieve employee's TODO list
        todo_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        todo_response = requests.get(todo_url)
        if todo_response.status_code != 200:
            print(f"Error: Could not fetch TODO list for user {username}")
        else:
            todo_data = todo_response.json()
            
            user_tasks = []
            for task in todo_data:
                task_completed_status = "Completed" if task['completed'] else "Incomplete"
                task_title = task['title']
                user_tasks.append({"username": username, "task": task_title, "completed": task_completed_status})
            
            all_employee_data[user_id] = user_tasks

    # Export to JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=2)

    print("Data for all employees has been exported to todo_all_employees.json.")

if __name__ == "__main__":
    get_all_employee_info()
