from environs import Env
import requests
from main_functions import get_image, get_extension


def get_nasa_days_pictures(token, count, dirname):

    url = "https://api.nasa.gov/planetary/apod/"
    payload = {
        "api_key": token,
        "count" : count,
    }
    response = requests.get(url, params = payload)
    response.raise_for_status()
    nasa_images = response.json()

    for index, nasa_image in enumerate(nasa_images):

        ext = get_extension(nasa_image["url"])
        file_name = f"{dirname}/apod_{index}{ext}"
        get_image(nasa_image["url"], file_name)


def main():
    
    env = Env()
    env.read_env()

    get_nasa_days_pictures(env.str("NASA_TOKEN"), 50, env.str('DIRECTORY'))


if __name__ == "__main__":
    main()