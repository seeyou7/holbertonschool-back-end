#!/usr/bin/python3
""" using rest api to get info """

import requests
import sys
import csv

if __name__ == "__main__":
    employee_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_data = requests.get(user_url).json()

    todo_url = (
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    )
    employee_tasks = requests.get(todo_url).json()

    with open("{}.csv".format(employee_id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee_tasks:
            taskwriter.writerow([employee_id, employee_data.get(
                'username'), task.get('completed'), task.get('title')])
