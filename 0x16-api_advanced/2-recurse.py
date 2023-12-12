#!/usr/bin/python3
"""Script that returns top 10 hot posts of a subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that returns a list of top posts"""
    headers = {'User-Agent': 'selBot/2.1'}
    URL = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    response = requests.get(URL, params=params, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            recurse(subreddit, hot_list, after=after_data)

        titles = response.json().get("data").get("children")
        for title in titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return None
