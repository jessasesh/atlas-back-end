#!/usr/bin/python3
"""
This script fetches user data and todo lists for all employees
from the JSONPlaceholder API and exports the data in JSON format.
"""
import json
import requests


def fetch_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
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

        return {employee_id: todo_list}
    else:
        return None


if __name__ == "__main__":
    all_employee_data = {}

    for employee_id in range(1, 11):  # Assuming employee IDs are from 1 to 10
        employee_data = fetch_employee_data(employee_id)
        if employee_data:
            all_employee_data.update(employee_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employee_data, json_file)
