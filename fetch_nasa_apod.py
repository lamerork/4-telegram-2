import os
import requests
from dotenv import load_dotenv
from main_functions import get_image, get_extension


def get_nasa_days_pictures(token, count):

    url = "https://api.nasa.gov/planetary/apod/"
    payload = {
        "api_key": token,
        "count" : count,
    }
    response = requests.get(url, params = payload)
    response.raise_for_status()
    nasa_json = response.json()

    for i, nasa in enumerate(nasa_json):

        ext = get_extension(nasa["url"])
        file_name = f"images/apod_{i}{ext}"
        get_image(nasa["url"], file_name)


def main():
    load_dotenv()
    count = 50
    get_nasa_days_pictures(os.environ["NASA_TOKEN"], count)


if __name__ == "__main__":
    main()