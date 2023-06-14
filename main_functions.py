import os
import requests
from urllib.parse import urlparse

def get_path_files(path):
    files_name = []
    for root, __, files in os.walk(path):
        for file in files:
            files_name.append(os.path.join(root, file))
    return files_name

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
