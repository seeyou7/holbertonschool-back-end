#!/usr/bin/python3
<<<<<<< HEAD
'''
Python script that returns information using REST API
'''
=======
"""Uses a REST API for a given employee ID, returns
information  about TODO list progress"""

>>>>>>> b6721a2d0666a8a0b4043541339be464004dd6b1
import requests
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    employee_id = sys.argv[1]
    user_url = (f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = requests.get(user_url).json()
    
    todos_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    employee_tasks = requests.get(todos_url).json()

    completed_tasks = [task for task in employee_tasks if task.get("completed")]
=======
    if len(sys.argv) != 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]
>>>>>>> b6721a2d0666a8a0b4043541339be464004dd6b1

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])
    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for title in TASK_TITLE:
        print("\t ", title)
