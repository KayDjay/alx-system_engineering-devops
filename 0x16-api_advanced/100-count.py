import requests
"""This is a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords"""
def count_words(subreddit, word_list, after=None, count_dict={}):
    """ This function count API words """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    
    headers = {"User-Agent": "Kaydee"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += 1
                    else:
                        count_dict[word.lower()] = 1
        
        after = data["data"]["after"]
        
        if after is not None:
            count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or no posts match.")
