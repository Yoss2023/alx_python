import requests
import sys

def get_employee_data(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_data, todos_data

def display_todo_progress(employee_name, completed_tasks, total_tasks, task_titles):
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in task_titles:
        print(f"\t{title}")

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Get employee data
    employee, todos = get_employee_data(employee_id)

    # Extract relevant information
    employee_name = employee.get('name')
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    total_tasks = len(todos)
    task_titles = [todo['title'] for todo in todos if todo['completed']]

    # Display the information
    display_todo_progress(employee_name, completed_tasks, total_tasks, task_titles)

if __name__ == "__main__":
    main()


