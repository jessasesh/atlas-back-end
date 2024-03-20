#!/usr/bin/python3
"""
This script to exports data in the CSV format.
"""
import requests
import sys
import csv


def get_username(user_id):
    """
    Retrieves the username associated with a given user ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP error
    return response.json().get('username', 'Unknown')


def get_todo_list(employee_id):
    """
    Retrieves the TODO list of a specific employee from the REST API.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP error
    return response.json()


def export_to_csv(employee_id, todo_list):
    """
    Exports the employee's TODO list to a CSV file.
    """
    # Open the CSV file for writing
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write the header row
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task to the CSV file
        for task in todo_list:
            username = get_username(task['userId'])
            writer.writerow([task['userId'], username,
                             task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list = get_todo_list(employee_id)

    export_to_csv(employee_id, todo_list)
