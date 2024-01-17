#!/usr/bin/python3
""" This function queries the Reddit API and returns the number of subscribers """

import requests

def number_of_subscribers(subreddit):
    """ This function queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Kaydee"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0