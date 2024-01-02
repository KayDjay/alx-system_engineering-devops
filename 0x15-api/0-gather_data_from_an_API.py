#!/usr/bin/python3
""" Get TODO list from REST API """

import requests
from sys import argv

if __name__ == '__main__':
    employeeId = argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employee_Name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get("completed") is True:
            done += 1
            done_tasks.append(task.get("title"))
    print(f"Employee {employee_Name} is done with tasks({done}/{len(tasks)}):")
    for i in done_tasks:
        print("\t ", i)