#!/usr/bin/python3

"""
queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    query the Reddit API with the subreddit parameter
    """
    url = f"https://www.reddit.com/subreddits/search.json?q={subreddit}"
    response = requests.get(url)
    subscriber = 0
    json_data = response.json()
    children = json_data['data']['children']
    for child in children:
        if (child['data']['title'] == subreddit):
            subscriber = child['data']['subscribers']

    return (int(subscriber))
