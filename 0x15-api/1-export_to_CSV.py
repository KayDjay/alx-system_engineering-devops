#!/usr/bin/python3
""" Get TODO list from REST API """

from requests import get
from sys import argv
import csv


if __name__ == "__main__":
    if len(argv) >= 2:
        user_id = get(f"https://jsonplaceholder.typicode.com/users"
                      f"/{argv[1]}")
        todos = get(f"https://jsonplaceholder.typicode.com/users"
                    f"/{argv[1]}/todos")
        if user_id.status_code == 200:
            Employee_name = user_id.json().get("username")
            data = todos.json()
            with open(f"{data[0].get('userId')}.csv", "w",
                      encoding="utf-8") as file:
                wr = csv.writer(file, quoting=csv.QUOTE_ALL)
                for i in data:
                    wr.writerow([
                        i.get('userId'),
                        Employee_name,
                        i.get('completed'),
                        i.get('title')
                        ]
                    )
