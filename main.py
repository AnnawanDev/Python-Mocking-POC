import requests


JOKE_URL = "http://api.icndb.com/jokes/random"


def get_joke():
    response = requests.get(JOKE_URL)

    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = "No jokes"

    return joke
