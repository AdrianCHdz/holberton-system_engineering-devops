#!/usr/bin/python3
"""This file will export the request to a CSV file
"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    import csv

    user = get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    url = get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    user = user.json()
    url = url.json()
    with open('{}.csv'.format(argv[1]), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for info in url:
            writer.writerow([argv[1], user['username'],
                             info['completed'], info['title']])
