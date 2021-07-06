import requests


def weather_in_your_city(city, api_key):
    resp = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}")
    print(resp.json())


def your_city():
    city = input("Write name of your city:\n")
    weather_in_your_city(city, "6c5e942e69803b89c78922251cae76b0")


if __name__ == '__main__':
    your_city()