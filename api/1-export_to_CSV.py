#!/usr/bin/python3
"""
Fetches data from an API
and returns information about the employee's todo list progress
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = f"https://jsonplaceholder.typicode.com/users/{userId}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    user_info = requests.get(user).json()
    todos_info = requests.get(todo).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, number_of_done_tasks, total_number_of_tasks))
    [print("\t " + task["title"]) for task in task_completed]


with open("USER_ID.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                     "TASK_TITLE"])
    # Write task rows
    for task in todos_info:
        writer.writerow([userId, employee_name, task["completed"],
                         task["title"]])
