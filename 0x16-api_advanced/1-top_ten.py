#!/usr/bin/python3
"""docs
"""
from requests import get


def top_ten(subreddit):
    """This function will get the hot posts of a subreddit
    """
    headers = {"User-Agent":
               "(Windows NT 10.0; Win64; x64) Chrome/70.0.3538.77"}
    url = get("https://www.reddit.com/r/{}/hot.json".
              format(subreddit), headers=headers, params={"limit": 10})
    if url.status_code == 200:
        children = url.json().get("data").get("children")
        for data in children:
            print(data.get("data").get("title"))
    else:
        print(None)
