#!/usr/bin/python3
"""
This script retrieves an employee's TODO list from the JSONPlaceholder API
and displays completed tasks in a formatted output.
"""

import requests
import sys


def main(employee_id):
    """Fetch and display an employee's TODO list progress."""
    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_response.raise_for_status()
    todos_response.raise_for_status()

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    completed_tasks = [t for t in todos if t.get("completed")]

    # Print first line
    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    main(emp_id)
