#!/usr/bin/python3
"""

This module represents a Python script that uses REST API to fetch and display
the TODO list progress of an employee.
"""


import json
import requests


def main():
    """This function defines how to fetch data from an API
    """
    # Fetch all username
    usr_url = "https://jsonplaceholder.typicode.com/users"
    user_resp = requests.get(usr_url)
    users = user_resp.json()

    all_data = {}

    for user in users:
        emp_id = user['id']
        username = user['username']

        # Fetch done tasks
        url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
        response = requests.get(url)
        todos = response.json()

        all_data[str(emp_id)] = [
                {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in todos
            ]

    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(all_data, f)


if __name__ == '__main__':
    main()
