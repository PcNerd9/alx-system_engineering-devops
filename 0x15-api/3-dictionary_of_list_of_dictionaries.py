#!/usr/bin/python3

"""
a script that get employees todos and print all his/her
completed todos
"""

import csv
import json
import requests


def main():
    """
    print the user profile and he/her completed todos
    """
    query = "https://jsonplaceholder.typicode.com/users/"
    r = requests.get(query)
    employee_profiles = json.loads(r.content)
    if not employee_profiles:
        return
    json_data = {}
    for employee in employee_profiles:
        r = requests.get("https://jsonplaceholder.typicode.com/todos/")
        todos = json.loads(r.content)
        userid = employee["id"]
        employee_todos = [detail for detail in todos
                          if detail['userId'] == userid]
        data = []
        for detail in employee_todos:
            dic = {}
            dic['username'] = employee['username']
            dic['task'] = detail['title']
            dic['completed'] = detail['completed']
            data.append(dic)
        json_data["{}".format(userid)] = data

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    main()
