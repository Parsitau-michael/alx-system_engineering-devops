#!/usr/bin/python3
""" This module represents a function that queries Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'SubCountApp:v1.0'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
