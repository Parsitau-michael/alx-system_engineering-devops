#!/usr/bin/python3
""" This module represents a recursive function that queries the Reddit API
and returns a list containing the titles of all hot
articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'SubCountApp:v1.0'
    }

    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        hot_list.extend([post['data']['title'] for post in posts])

        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
