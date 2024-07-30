#!/usr/bin/python3
"""

This module represents a Python script that uses REST API to fetch and display
the TODO list progress of an employee.
"""


import csv
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
    name = user['name']

    # Exporting the data into CSV format
    filename = "{}.csv".format(emp_id)

    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)

        for todo in todos:
            writer.writerow([emp_id, name, todo['completed'], todo['title']])


if __name__ == '__main__':
    main()
