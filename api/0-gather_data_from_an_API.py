#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Fetches TODO list progress for a given employee ID from the JSONPlaceholder REST API
and displays completed tasks in the required format.
"""

import requests
import sys


def fetch_employee_todos(employee_id):
    """
    Fetch employee info and TODO list from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: (employee_name, list_of_completed_tasks, total_tasks_count)
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    done_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)

    return employee_name, done_tasks, total_tasks


def main():
    """Main function that parses arguments and prints TODO list progress."""
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <employee_id>")

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Employee ID must be an integer")

    employee_name, done_tasks, total_tasks = fetch_employee_todos(employee_id)
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    main()
