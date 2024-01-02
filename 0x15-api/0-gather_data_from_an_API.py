#!/usr/bin/python3

""" Get TODO list from REST API """


from requests import get
from sys import argv


def getdata(data=[], done=False):
    """
    print only completed tasks or return the count
    of completed and total tasks,
    """
    if done is True:
        for a in data:
            if a.get("completed") is True:
                print("\t ", a.get("title"))
    else:
        done = 0
        total = len(data)
        if not data:
            return (done, total)
        for a in data:
            if a.get("completed") is True:
                done += 1
        return (done, total)


if __name__ == "__main__":
    if len(argv) >= 2:
        user_id = get(f"https://jsonplaceholder.typicode.com/users"
                      f"/{argv[1]}")
        todos = get(f"https://jsonplaceholder.typicode.com/users"
                    f"/{argv[1]}/todos")
        if user_id.status_code == 200:
            EMPLOYEE_NAME = user_id.json().get("name")
            data = todos.json()
            NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS = getdata(data)
            print(f"Employee {EMPLOYEE_NAME} is done with tasks("
                  f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
            getdata(data, True)
