#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
prints the count of occurrences of each word in the word_list
in the titles of all hot articles for a given subreddit.
"""
import requests

def count_words(subreddit, word_list, after='', word_count={}):
    """
    Queries the Reddit API and prints the count of occurrences of each word in the word_list
    in the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of words to count in the titles.
        after (str): The 'after' parameter for pagination (default is '').
        word_count (dict): Dictionary to store the count of words (default is {}).

    Returns:
        None
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    
    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # If the response status is not 200, return (invalid subreddit or other error)
    if response.status_code != 200:
        return
    
    # Parse the JSON response
    data = response.json().get('data', {})
    after = data.get('after', None)  # Get the 'after' token for pagination
    posts = data.get('children', [])  # Get the list of posts
    
    # Process each post title
    for post in posts:
        title = post['data']['title'].lower().split()  # Convert title to lowercase and split into words
        for word in word_list:
            word_lower = word.lower()
            word_count[word_lower] = word_count.get(word_lower, 0) + title.count(word_lower)
    
    # If there is an 'after' token, recursively call count_words to process the next page
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        # Sort the word counts by count (descending) and alphabetically (ascending)
        sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f'{word}: {count}')
