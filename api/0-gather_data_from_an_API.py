#!/usr/bin/python3
"""
Python script that, for a given employee ID, returns
information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_name(employee_id):
    """ Returns employee name from specific ID """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(employee_id)
    response = requests.get(url)
    employee_data = response.json()
    return employee_data.get("name")


def get_employee_tasks(employeeId):
    """ Returns all tasks associated with an employee """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(employeeId)
    response = requests.get(url)
    return response.json()


def get_completed_tasks(employeeName, completedTasks, totalTasks):
    """ Prints all tasks by employee ID """
    print("Employee {} is done with tasks({}/{}):".format
          (employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("  {}".format(task.get("title")))


def print_employee_tasks(tasks):
    """ Returns all completed tasks """
    completed_tasks = []

    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)
    return completed_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employeeId = sys.argv[1]
    tasks = get_employee_tasks(employeeId)
    employeeName = get_employee_name(employeeId)
    completedTasks = print_employee_tasks(tasks)
    get_completed_tasks(employeeName, completedTasks, len(tasks))