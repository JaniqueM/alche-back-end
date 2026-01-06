#!/usr/bin/python3
"""
1-export_to_CSV.py

Fetches TODO list progress for a given employee ID from the JSONPlaceholder
REST API and exports all tasks to a CSV file.
"""

import csv
import requests
import sys


def fetch_employee_todos(employee_id):
    """
    Fetch employee info and TODO list from the API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: (employee_id, employee_name, todos)
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee information
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()
    employee_name = user_data.get("username")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos = todos_response.json()

    return employee_id, employee_name, todos


def export_to_csv(employee_id, employee_name, todos):
    """
    Export tasks to a CSV file in the required format.

    Args:
        employee_id (int): The ID of the employee.
        employee_name (str): The username of the employee.
        todos (list): List of task dictionaries.
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                task.get("completed"),
                task.get("title")
            ])


def main():
    """Main function that parses arguments and exports tasks to CSV."""
    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <employee_id>")

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Employee ID must be an integer")

    employee_id, employee_name, todos = fetch_employee_todos(employee_id)
    export_to_csv(employee_id, employee_name, todos)


if __name__ == "__main__":
    main()
