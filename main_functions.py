import os
import requests
from urllib.parse import urlparse


def create_dirs(dirname):
        os.makedirs(dirname, exist_ok=True)

def get_image(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    url_parsed = urlparse(url)
    return os.path.splitext(url_parsed.path)[1]


def main():
    dir_name = "images"
    
    create_dirs(dir_name)

if __name__ == "__main__":
    main()
