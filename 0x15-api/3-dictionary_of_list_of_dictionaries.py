#!/usr/bin/python3
"""docs
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    import json

    user = get(
        'https://jsonplaceholder.typicode.com/users')
    url = get(
        'https://jsonplaceholder.typicode.com/todos')
    user = user.json()
    url = url.json()
    new_dict = {}
    for info in user:
        info_list = []
        for alls in url:
            c_dict = {}
            if (alls["userId"] is info["id"]):
                c_dict["username"] = info["username"]
                c_dict["task"] = alls["title"]
                c_dict["completed"] = alls["completed"]
                info_list.append(c_dict)
        new_dict[info['id']] = info_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(new_dict, f)
