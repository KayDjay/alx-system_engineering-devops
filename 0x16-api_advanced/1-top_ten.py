#!/usr/bin/python3
""" This function that queries the Reddit API and prints the titles of
    the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ This function that queries the Reddit API
        and prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Kaydee"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
