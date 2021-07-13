import multiprocessing
import threading
import json
import requests


thread_local = threading.local()





def reddit_comments(url, subreddit):
    resp = requests.get(url, {"subreddit": subreddit})
    data = resp.json()
    with open("data.json", "w") as file:
        json.dump(data, file)

if __name__ == '__main__':
    processes = [multiprocessing.Process(target=reddit_comments("https://api.pushshift.io/reddit/comment/search/", subreddit="NoFap")) for _ in range(10)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

