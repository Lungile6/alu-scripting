#!/usr/bin/python3
"""Return a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """A list of titles of hot articles """
    if hot_list is None:
        hot_list = []

    # Construct the URL for the Reddit API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0
                                      Win64
                                      x64)
        AppleWebKit / 537.36 (KHTML, like Gecko)
        Chrome / 126.0.0.0 Safari / 537.36'}
    params = {'after': after, 'limit': 100}

    # Make the API request
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    # Check if the response status code is not 200 (OK)
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json().get('data', {})
    children = data.get('children', [])

    # If there are no children, return the accumulated hot_list
    if not children:
        return hot_list

    # Append the titles of the hot articles to the hot_list
    for child in children:
        hot_list.append(child['data']['title'])

    # Get the 'after' parameter for the next page
    after = data.get('after')

    # If there is no 'after' parameter, return the accumulated hot_list
    if after is None:
        return hot_list

    # Recursively call the function with the updated 'after' parameter
    return recurse(subreddit, hot_list, after)