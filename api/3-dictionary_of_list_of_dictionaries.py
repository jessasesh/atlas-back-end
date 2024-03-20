#!/usr/bin/python3
"""
This script fetches user data and todo list for a given employee ID
from the JSONPlaceholder API and exports the data in JSON format.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        exit()

    employeeId = argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employeeId}"
    todos_url = f"{base_url}/todos?userId={employeeId}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get("username")

    todo_list = []
    for task in todos_data:
        todo_list.append({
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    output_data = {employeeId: todo_list}

    with open("todo_all_employees.json", "a") as json_file:
        json.dump(output_data, json_file)
        json_file.write("\n")
