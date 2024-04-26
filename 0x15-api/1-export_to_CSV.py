#!/usr/bin/python3

"""
a script that get employees todos and print all his/her
completed todos
"""

import csv
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

    data = []
    for detail in employee_todos:
        dic = {}
        dic['userid'] = "{}".format(employee_profile['id'])
        dic['Username'] = "{}".format(employee_profile['username'])
        dic['Status'] = "{}".format(detail['completed'])
        dic['Title'] = "{}".format(detail['title'])
        data.append(dic)
    fieldnames = ["userid", "Username", "Status", "Title"]
    with open("{}.csv".format(userid), "w") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

        csvwriter.writerows(data)


if __name__ == "__main__":
    main()
