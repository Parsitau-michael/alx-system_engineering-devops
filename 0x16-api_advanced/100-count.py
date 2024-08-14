#!/usr/bin/python3
""" This module represents a recursive function that queries
the Reddit API parses the title of all hot articles,
and prints a sorted count of given keywords.
"""


import requests


def count_words(subreddit, word_list, after=None, word_count={}):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'SubCountApp:v1.0'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        if not word_count:
            word_count = {word.lower(): 0 for word in word_list}

        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_lower = word.lower()
                word_count[word_lower] += title.count(word_lower)

        after = data['data'].get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = dict(sorted(word_count.items(),
                                     key=lambda x: (-x[1], x[0])))
            for word, count in sorted_word_count.items():
                if count > 0:
                    print("{}: {}".format(word, count))
    else:
        return None
