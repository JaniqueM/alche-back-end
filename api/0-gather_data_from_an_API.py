#!/usr/bin/python3
"""
Script that retrieves an employee's TODO list from the JSONPlaceholder API
and displays completed tasks in a formatted output.
"""

import sys
import requests

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get("completed")]

    # First line
    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )

    # Completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
