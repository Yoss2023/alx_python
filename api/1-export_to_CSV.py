import requests
import sys
import csv

"""     Using what you did in the task #0, extend your Python script to export data in the CSV format."""

def get_employee_data(employee_id):
    
""" Get employee details """


    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    
    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_data, todos_data

def export_to_csv(employee_id, employee_name, todos):

""" function to export data to csv """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos:
            writer.writerow([employee_id, employee_name, str(todo['completed']), todo['title']])

    print(f"Data exported to {filename}")

def main():
    
    """ the main function """

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Get employee data
    employee, todos = get_employee_data(employee_id)

    # Extract relevant information
    employee_name = employee.get('name')

    # Display the information
    export_to_csv(employee_id, employee_name, todos)

if __name__ == "__main__":
    main()

