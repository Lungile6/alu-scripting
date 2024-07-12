#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Returns the number of subscribers for a given subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit. """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = \
        {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/126.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
        
if __name__ == '__main__':
    print(number_of_subscribers)('programming')
    print(number_of_subscribers)('not_a_valid_subreddit')
