#!/usr/bin/python3
"""
This script fetches employee data from a public API (jsonplaceholder.typicode.com)
and displays their completed tasks.

Usage: python script.py <Employee_id>
"""
import requests
import sys

def main(Employee_id):
    response_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{Employee_id}')

    if response_user.status_code == 200:
        user_data = response_user.json()
        Employee_name = user_data['name']
    else:
        print("URL input error for user")
        sys.exit(1)  # Exit if we can't fetch the user data
    
    response_todos = requests.get(f'https://jsonplaceholder.typicode.com/todos/?userId={Employee_id}')

    if response_todos.status_code == 200:
        user_todo = response_todos.json()
        to_do = [task for task in user_todo if task['completed']]
        tasks = len(user_todo)
        Completed_tasks = len(to_do)
        print(f"Employee {Employee_name} is done with tasks ({Completed_tasks}/{tasks}):")
        for task in to_do:
            print(f"\t {task['title']}")
    else:
        print("URL input error for todos")
        sys.exit(1) 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <Employee_id>")
        sys.exit(1)

    Employee_id = int(sys.argv[1])
    main(Employee_id)
