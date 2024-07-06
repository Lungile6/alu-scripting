#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """prints the titles of the top ten hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = f"http://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            
            for post in posts:
                print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        print(None)
    except ValueError:
        print("Invalid JSON response")
        print(None)
