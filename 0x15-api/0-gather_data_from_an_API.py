#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = sys.argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get employee name
    response = requests.get(api_url)
    if response.status_code != 200:
        print("Error: Could not retrieve employee information")
        exit(1)
    employee = response.json()
    employee_name = employee["name"]

    # Get employee todo list
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Could not retrieve todo list")
        exit(1)
    todos = response.json()
    completed_todos = [todo["title"] for todo in todos if todo["completed"]]
    total_todos = len(todos)
    done_todos = len(completed_todos)

    # Print employee todo list progress
    print(f"Employee {employee_name} is done with tasks({done_todos}/{total_todos}):")
    for todo in completed_todos:
        print(f"\t {todo}")

