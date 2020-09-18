#!/usr/bin/python3
"""docs
"""
from requests import get


def number_of_subscribers(subreddit):
    headers = {"User-Agent":
               "(Windows NT 10.0; Win64; x64) Chrome/70.0.3538.77"}
    url = get("https://www.reddit.com/r/{}/about.json".
              format(subreddit), headers=headers)
    if (url.status_code != 200):
        return 0
    else:
        return url.json()["data"]["subscribers"]
