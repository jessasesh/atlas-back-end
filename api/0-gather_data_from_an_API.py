#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns
information about his/her TODO list progress.
"""

import sys
import requests


def get_todo_list(employee_id):
    """
    Retrieves the TODO list of a specific employee from the REST API.
    """
    url = (
        "https://jsonplaceholder.typicode.com/"
        f"users/{employee_id}/todos"
    )
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP error
    return response.json()


def print_todo_list_progress(employee_name, completed_tasks, total_tasks):
    """
    Prints the progress of an employee's TODO list.
    """
    progress_message = (
        f"Employee {employee_name} is done with "
        f"tasks({len(completed_tasks)}/{total_tasks}):"
    )
    print(progress_message)
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = get_todo_list(employee_id)

    completed_tasks = [task for task in todo_list if task['completed']]
    employee_name = todo_list[0]['name']
    total_tasks = len(todo_list)

    print_todo_list_progress(employee_name, completed_tasks, total_tasks)
