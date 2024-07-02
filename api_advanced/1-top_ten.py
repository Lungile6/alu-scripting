#!/usr/bin/python3

"""
This module contains a function that queries the Reddit API and 
returns the top 10 hot posts for a given subreddit.
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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set the User-Agent header to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json() 
        
        # Extract the list of posts
        posts = data.get('data', {}).get('children', [])
        
        # Print the title of each post
        for post in posts:
            print(post.get('data', {}).get('title'))
    else:
        # Print None if the subreddit is invalid or the request failed
        print(None)
