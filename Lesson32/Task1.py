import requests



resp = requests.get("https://en.wikipedia.org/w/api.php")

data = resp.text
with open("robot.txt", "w") as file:
    file.write(data)