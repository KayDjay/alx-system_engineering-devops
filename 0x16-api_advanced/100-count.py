#!/usr/bin/python3
""" This is a recursive function that queries Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords """

import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """ This function count API words """
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.\
            format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.\
            format(subreddit, after)

    headers = {'User-Agent': 'Kaydee'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get('after')
        children = data.get('children')

        for child in children:
            title = child.get('data').get('title').lower()
            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word in count_dict:
                        count_dict[word] += count
                    else:
                        count_dict[word] = count

        if after is not None:
            count_words(subreddit, word_list, after,
                        count_dict)
        else:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print('{}: {}'.format(word, count))
    else:
        return    