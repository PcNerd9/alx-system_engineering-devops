#!/usr/bin/python3

"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot post listed for a given
    subreddit
    """
    url = "https://www.reddit.com/r/{}/new.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    count = 0
    json_data = response.json()
    data = json_data.get('data', None)
    if data is None:
        print(None)
        return
    children = data.get('children', None)
    if children is None:
        print(None)
        return
    for child in children:
        if (count >= 10):
            break
        count = count + 1
        if (child['data']['subreddit'] == subreddit):
            print(child['data']['title'])
