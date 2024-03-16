#!/usr/bin/python3
"""
 Script that returns to-do list progress
 info about specified employee.
"""

import requests
import sys


def emp_todo(employeeId):
    """
    Returns all tasks associated with an employee.
    """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}/todos".format(employeeId)
    response = requests.get(url)
    return response.json()


def emp_name(employeeId):
    """
    Returns employee name.
    """
    url = "https://jsonplaceholder.typicode.com/"
    url += "users/{}".format(employeeId)
    response = requests.get(url)
    return response.json().get("name")


def comp_tasks(tasks):
    """
    Returns number of completed tasks by specified employee.
    """
    completed_tasks = []

    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)
    return completed_tasks


def print_emp_tasks(employeeName, completedTasks, totalTasks):
    """
    Prints all tasks belonging to specified employee.
    """
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    employeeId = sys.argv[1]
    tasks = emp_todo(employeeId)
    employeeName = emp_name(employeeId)
    completedTasks = comp_tasks(tasks)
    print_emp_tasks(employeeName, completedTasks, len(tasks))
