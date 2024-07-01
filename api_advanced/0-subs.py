#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        int: The number of subscribers if the subreddit is valid, otherwise 0.
    """
    # Construct the URL for the subreddit's about.json page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    # Make the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # Return 0 if the subreddit is invalid or the request failed
        return 0

# Example usage: print the number of subscribers for the 'reddit' subreddit
print(number_of_subscribers('reddit'))