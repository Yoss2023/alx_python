import requests
import sys
import json

def get_employee_data(employee_id):
    # Get employee details from the API
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Get employee's TODO list from the API
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_data, todos_data

def export_to_json(employee_id, employee_name, todos):
    # Create a JSON file with the specified format
    filename = f"{employee_id}.json"

    data = {str(employee_id): [{"task": todo['title'], "completed": todo['completed'], "username": employee_name} for todo in todos]}

    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Get employee data from the API
    employee, todos = get_employee_data(employee_id)

    # Extract relevant information
    employee_name = employee.get('name')

    # Display the information and export to JSON
    export_to_json(employee_id, employee_name, todos)

if __name__ == "__main__":
    main()

