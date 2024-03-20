#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-dictionary_of_list_of_dictionaries.py <employeeId>")
        sys.exit(1)

    employeeId = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(employeeId)
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employeeId)

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    if response_user.status_code != 200:
        print("User not found")
        sys.exit(1)
    if response_todos.status_code != 200:
        print("Todos not found")
        sys.exit(1)

    user_data = response_user.json()
    todos_data = response_todos.json()

    username = user_data.get('username')

    tasks = []
    for todo in todos_data:
        task = {
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed')
        }
        tasks.append(task)

    output = {employeeId: tasks}

    with open('todo_all_employees.json', 'a') as file:
        json.dump(output, file)
    