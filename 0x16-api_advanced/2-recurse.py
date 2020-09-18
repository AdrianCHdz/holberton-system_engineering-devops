#!/usr/bin/python3
"""docs
"""
from requests import get


def recurse(subreddit, hot_list=[], children=None):
    """This function will get the hot posts of a subreddit
    """
    headers = {"User-Agent":
               "(Windows NT 10.0; Win64; x64) Chrome/70.0.3538.77"}
    url = get("https://www.reddit.com/r/{}/hot.json?after={}".
              format(subreddit, children), headers=headers)
    if url.status_code == 200:
        children = url.json().get("data").get("after")
        parent = url.json().get("data").get("children")
        for data in parent:
            hot_list.append(data.get("data").get("title"))
        if children is not None:
            recurse(subreddit, hot_list, children)
        return hot_list
    else:
        return None
