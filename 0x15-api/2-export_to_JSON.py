#!/usr/bin/python3
"""docs
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    import json

    user = get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    url = get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    user = user.json()['username']
    url = url.json()
    info_list = []
    for info in url:
        c_dict = {}
        for key, value in info.items():
            if key == "title":
                c_dict["task"] = value
            if key == "completed":
                c_dict[key] = value
        c_dict['username'] = user
        info_list.append(c_dict)
    new_dict = {argv[1]: info_list}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(new_dict, f)
