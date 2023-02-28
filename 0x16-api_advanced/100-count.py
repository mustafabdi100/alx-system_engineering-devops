import requests
import re

def count_words(subreddit, word_list, count_dict=None, after=None):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        count_dict (dict): The dictionary to store the count of each word.
        after (str): The parameter for the next page of the API results.
    """
    if count_dict is None:
        count_dict = {}
        word_list = [word.lower() for word in word_list]

    user_agent = {'User-agent': 'test45'}
    posts = requests.get(f'http://www.reddit.com/r/{subreddit}/hot.json?after={after}',
                         headers=user_agent)

    if posts.status_code != 200:
        return

    posts = posts.json()['data']
    aft = posts['after']
    posts = posts['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if re.search(fr"(?<!\S){word}(?!\S)", title):
                count_dict[word] = count_dict.get(word, 0) + 1

    if aft is not None:
        count_words(subreddit, word_list, count_dict, aft)
    else:
        for word, count in sorted(count_dict.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word}: {count}")

