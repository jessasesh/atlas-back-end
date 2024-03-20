#!/usr/bin/python3
"""
Python script that, for a given employee ID, exports
TODO list progress in JSON format.
"""

import json
import requests
import sys


def get_employee_name(employee_id):
    """
    Retrieves the name of the employee from the REST API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP error
    return response.json().get('name', 'Unknown')


def get_todo_list(employee_id):
    """
    Retrieves the TODO list of a specific employee from the REST API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP error
    return response.json()


def export_to_json(employee_id, employee_name, todo_list):
    """
    Exports the TODO list of an employee to a JSON file.
    """
    data = {
        str(employee_id): [
            {"task": task['title'], "completed": task['completed'],
             "username": employee_name}
            for task in todo_list
        ]
    }
    with open(f"{employee_id}.json", "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name = get_employee_name(employee_id)
    todo_list = get_todo_list(employee_id)

    export_to_json(employee_id, employee_name, todo_list)
