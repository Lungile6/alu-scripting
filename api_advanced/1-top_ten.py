#!/usr/bin/python3
"""
Print top ten hot posts!
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the top 10 hot posts or
        None if the subreddit is invalid.
    """
    # Construct the URL to fetch the top 10 hot posts from the subreddit
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # Set the User-Agent header to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

    try:
        # Make a GET request to the Reddit API to fetch the top hot posts
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)

        # Parse the JSON response and extract the list of hot posts
        HOT_POSTS = RESPONSE.json().get("data").get("children")

        # Iterate over the list of hot posts and print the title of each post
        [print(post.get('data').get('title')) for post in HOT_POSTS]
    except Exception:
        # If any exception occurs, print None to indicate an error
        print(None)
