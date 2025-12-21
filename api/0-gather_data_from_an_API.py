#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    completed_tasks = [t for t in todos if t.get("completed") is True]

    # Output
    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{len(todos)}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
