from environs import Env
import requests
import argparse
from main_functions import get_image

def fetch_spacex_last_launch(directory, launch_id):

   
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    urls = response.json()["links"]["flickr"]["original"]

    for index, url in enumerate(urls):
        get_image(url, f"{directory}/spacex{index}.jpg")


def main():

    env = Env()
    env.read_env()
    
    parser = argparse.ArgumentParser(description="Программа скачивает картинки запуска ракет SpaceX")
    parser.add_argument("-id", help="ID Запуска ракеты", default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()


    fetch_spacex_last_launch(env.str('DIRECTORY'), args.id)


if __name__ == '__main__':
    main()