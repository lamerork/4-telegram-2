import requests
import argparse
from main_functions import get_image


def fetch_spacex_last_launch():

    parser = argparse.ArgumentParser(description="Программа скачивает картинки запуска ракет SpaceX")
    parser.add_argument("-id", help="ID Запуска ракеты", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()

    print(args)

    response = requests.get(f"https://api.spacexdata.com/v5/launches/{args.id}")
    response.raise_for_status()
    urls = response.json()["links"]["flickr"]["original"]

    for i, url in enumerate(urls):
        get_image(url, f"images/spacex{i}.jpg")


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()