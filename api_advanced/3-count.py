#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
prints the count of occurrences of each word in the word_list
in the titles of all hot articles for a given subreddit.
"""
import requests


def count_words(subreddit, word_list, after='', word_count=None):
    """
    Queries the Reddit API and prints the count of
    occurrences of each word in the word_list
    in the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to count in the titles.
        after (str): The 'after' parameter for pagination (default is '').
        word_count (dict): Dictionary to store
        the count of words (default is None)
    Returns:
        None
    """
    if word_count is None:
        word_count = {}

    headers = {
        'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0
                                      Win64
                                      x64) AppleWebKit / 537.36
        (KHTML, like Gecko) Chrome / 58.0.3029.110 Safari / 537.3'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after, 'limit': 100}

    # Make a GET request to the Reddit API
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)

    # If the response status is not 200, return (invalid subreddit or other
    # error)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return

    # Parse the JSON response
    data = response.json().get('data', {})
    after = data.get('after', None)  # Get the 'after' token for pagination
    posts = data.get('children', [])  # Get the list of posts

    # Debugging: Print the number of posts retrieved
    print(f"Retrieved {len(posts)} posts")

    # Process each post title
    for post in posts:
        # Convert title to lowercase and split into words
        title = post['data']['title'].lower().split()
        # Debugging: Print the title of each post
        print(f"Processing title: {title}")
        for word in word_list:
            word_lower = word.lower()
            count = title.count(word_lower)
            if count > 0:
                print(
                    f"Found {count} occurrences of word
                    '{word_lower}' in title: {title}")
            word_count[word_lower] = word_count.get(word_lower, 0) + count

    # If there is an 'after' token, recursively call count_words to process
    # the next page
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        # Sort the word counts by count (descending) and alphabetically
        # (ascending)
        sorted_word_count = sorted(
            word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f'{word}: {count}')
