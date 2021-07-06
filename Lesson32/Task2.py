import requests
import json


def get_data(url, params):
    r = requests.get(url, params)
    return r.json()


data = get_data("https://api.pushshift.io/reddit/comment/search/", {"subreddit": "Nationals", "sort": "desc", "sort_type": "created_utc", "size": 20})

with open("reddit.json", "w") as file:
    json.dump(data, file)
