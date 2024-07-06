#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
    r = requests.get(
        'http://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/126.0.0.0 Safari/537.36"
        },
        params={
            'limit': 10
        },
        allow_redirects=False
    ).json()
    posts = r.get('data', {}).get('children', None)
    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
    else:
        for post in posts:
            print(post.get('data', {}).get('title', None))
