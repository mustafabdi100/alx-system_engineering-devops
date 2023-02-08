#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        response = requests.get(url)
        if response.status_code == 200:
            user = response.json()
            employee_name = user.get("name")

            url = "https://jsonplaceholder.typicode.com/todos"
            response = requests.get(url)
            if response.status_code == 200:
                todos = response.json()
                done_todos = [todo for todo in todos if todo.get("userId") == user_id and todo.get("completed") is True]
                done_todos_count = len(done_todos)
                total_todos_count = len(todos)

                print("Employee {} is done with tasks({}/{}):".format(employee_name, done_todos_count, total_todos_count))
                for todo in done_todos:
                    print("\t {}".format(todo.get("title")))
        else:
            print("Error: status code {}".format(response.status_code))
    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
