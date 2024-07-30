#!/usr/bin/python3
"""

This module represents a Python script that uses REST API to fetch and display
the TODO list progress of an employee.
"""


import json
import requests
from sys import argv, exit


def main():
    """This function defines how to fetch data from an API
    """
    if len(argv) != 2:
        exit(1)

    emp_id = int(argv[1])

    # Fetch done tasks
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(emp_id)
    response = requests.get(url)
    todos = response.json()

    total_tasks = len(todos)
    done_tasks = [todo for todo in todos if todo['completed']]
    total_done = len(done_tasks)

    # Fetch name
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    user_resp = requests.get(usr_url)
    user = user_resp.json()
    name = user['username']

    formatted_data = {
            str(emp_id): [
                {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": name
                }
                for todo in todos
            ]
        }

    filename = "{}.json".format(emp_id)
    with open(filename, 'w') as f:
        json.dump(formatted_data, f)


if __name__ == '__main__':
    main()
