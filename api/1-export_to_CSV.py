#!/usr/bin/python3
"""
1-export_to_CSV.py

Fetches all tasks for a given employee ID from the JSONPlaceholder REST API
and exports them to a CSV file in the required format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys


def fetch_employee_and_todos(employee_id):
    """
    Fetch employee info and all their TODOs from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: (user_id, username, todos)
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos"

    # Fetch employee information
    user_resp = requests.get(user_url)
    user_resp.raise_for_status()
    user = user_resp.json()

    user_id = user.get("id")
    username = user.get("username")

    # Fetch all tasks for this user (owned tasks)
    todos_resp = requests.get(todos_url, params={"userId": employee_id})
    todos_resp.raise_for_status()
    todos = todos_resp.json()

    return user_id, username, todos


def export_to_csv(user_id, username, todos):
    """
    Export tasks to a CSV file in the required format.

    Args:
        user_id (int): The user ID from the API.
        username (str): The username from the API.
        todos (list): List of task dictionaries.
    """
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(user_id),
                str(username),
                str(task.get("completed")),
                str(task.get("title"))
            ])


def main():
    """Parse CLI arguments and export the user's tasks to CSV."""
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <employee_id>")

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Employee ID must be an integer")

    user_id, username, todos = fetch_employee_and_todos(employee_id)

    if user_id is None or username is None:
        sys.exit("Employee not found")

    export_to_csv(user_id, username, todos)


if __name__ == "__main__":
    main()
