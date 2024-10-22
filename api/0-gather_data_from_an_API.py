#!/usr/bin/python3
"""
This script fetches employee data from a public API (jsonplaceholder.typicode.com)
and displays their completed tasks.

Usage: python script.py <Employee_id>
"""

import requests
import sys


def main(employee_id):
    """
    Main function that fetches user and tasks data from the API.
    Prints the completed tasks for the given employee.
    """
    response_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')

    if response_user.status_code == 200:
        user_data = response_user.json()
        employee_name = user_data['name']
    else:
        print("URL input error for user")
        sys.exit(1)  # Exit if we can't fetch the user data
    
    response_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    if response_todos.status_code == 200:
        user_todo = response_todos.json()
        completed_tasks = [task for task in user_todo if task['completed']]
        total_tasks = len(user_todo)
        completed_count = len(completed_tasks)
        print(f"Employee {employee_name} is done with tasks ({completed_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task['title']}")
    else:
        print("URL input error for todos")
        sys.exit(1)  # Exit if we can't fetch the todos data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    main(employee_id)
