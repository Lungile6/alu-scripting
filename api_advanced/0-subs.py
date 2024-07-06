#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of
    subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit is valid,
        otherwise 0.
    """
    # Construct the URL for the subreddit's about.json page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0

    except requests.RequestException as e:
        # Handle any request exceptions (e.g., network issues)
        print(f"An error occurred: {e}")
        return 0
