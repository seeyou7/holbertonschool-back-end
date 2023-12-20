#!/usr/bin/python3
"""script using a REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {__file__} employee_id(int)")
        sys.exit(1)

    BASE_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = int(sys.argv[1])

    """ Fetch todo list of an employee"""
    EMPLOYEE_TODOS = requests.get(f"{BASE_URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    TODO_DATA = EMPLOYEE_TODOS.json()
    EMPLOYEE_NAME = TODO_DATA[0]["user"]["name"]

    """Calculate TODO list and completed todo list """
    TOTAL_NUMBER_OF_TASKS = len(TODO_DATA)
    NUMBER_OF_DONE_TASKS = sum(1 for task in TODO_DATA if task["completed"])
    TASK_TITLE = [task["title"] for task in TODO_DATA if task["completed"]]

    """Display progress information"""
    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    """Display titles of completed tasks"""""
    for title in TASK_TITLE:
        print("\t", title)
