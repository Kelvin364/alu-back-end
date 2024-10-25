#!/usr/bin/python3
"""
This script fetches data from a REST API for a given user ID,
and exports the user's list information to a JSON file.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    # Mapping the URLs-endpoints and using the GET method
    user_id = argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    # Fetch user data
    user_data = requests.get(f"{base_url}users/{user_id}")
    todos_data = requests.get(f"{base_url}todos?userId={user_id}")

    # Convert fetched data to JSON format
    user = user_data.json()
    user_todo = todos_data.json()
    employee_name = user["name"]

    # Prepare data to export to JSON format
    export_data = {
        user_id: [{
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        } for task in user_todo]
    }

    # Save data to JSON file
    with open(f"{user_id}.json", 'w') as json_file:
        json.dump(export_data, json_file, indent=4)
