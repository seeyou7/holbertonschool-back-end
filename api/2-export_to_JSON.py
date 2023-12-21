#!/usr/bin/python3
"""Uses a REST API for a given employee ID, returns
information about TODO list progress and exports in jSON"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = sys.argv[1]

    EMPLOYEE_TODOS = requests.get(f"{URL}/users/{EMPLOYEE_ID}/todos",
                                  params={"_expand": "user"})
    data = EMPLOYEE_TODOS.json()

    if not data:
        print(f"No data found for employee ID {EMPLOYEE_ID}")
        sys.exit(1)

    username = data[0]["user"]["username"]
    USER_TASK = {EMPLOYEE_ID: []}
    for task in data:
        dic_task = {"task": task["title"], "completed": task["completed"],
                    "username": username}
        USER_TASK[EMPLOYEE_ID].append(dic_task)

    fileName = f"{EMPLOYEE_ID}.json"
    with open(fileName, "w") as file:
        json.dump(USER_TASK, file)
