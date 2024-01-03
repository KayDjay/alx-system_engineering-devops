#!/usr/bin/python3

"""
 REST-API of a given employee ID to returns
information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json


if __name__ == "__main__":
    if len(argv) >= 2:
        user_id = get(f"https://jsonplaceholder.typicode.com/users"
                      f"/{argv[1]}")
        todos = get(f"https://jsonplaceholder.typicode.com/users"
                    f"/{argv[1]}/todos")
        if user_id.status_code == 200:
            Employee_name = user_id.json().get("username")
            data = todos.json()
            with open(f"{data[0].get('userId')}.json", "w",
                      encoding="utf-8") as file:
                main = {}
                dict_list = []
                for i in data:
                    dict_list.append({
                        "task": i.get('title'),
                        "completed": i.get('completed'),
                        "username": Employee_name
                        })
                main[i.get('userId')] = dict_list
                file.write(json.dumps(main))
