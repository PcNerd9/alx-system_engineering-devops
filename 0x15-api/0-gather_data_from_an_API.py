#!/usr/bin/python3

"""
a script that get employees todos and print all his/her
completed todos
"""


import json
import requests
import sys


def main():
    """
    print the user profile and he/her completed todos
    """
    userid = int(sys.argv[1])
    query = "https://jsonplaceholder.typicode.com/users/{}".format(userid)
    r = requests.get(query)
    employee_profile = json.loads(r.content)
    if not employee_profile:
        return
    employee_name = employee_profile['name']
    r = requests.get("https://jsonplaceholder.typicode.com/todos/")
    todos = json.loads(r.content)
    employee_todos = [detail for detail in todos if detail['userId'] == userid]
    todos_lenght = len(employee_todos)
    completed_todos = [detail for detail in employee_todos
                       if detail['completed'] is True]
    completed_task_len = len(completed_todos)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_task_len, todos_lenght))
    for todo in completed_todos:
        print(f"\t {todo['title']}")


if __name__ == "__main__":
    main()
