import requests

""" This is a function that queries Reddit API and return a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return a list containing the titles of all hot articles for a given subreddit
"""

def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Kaydee"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title")
            hot_list.append(title)
        
        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
