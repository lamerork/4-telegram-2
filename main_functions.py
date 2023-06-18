import os
import requests
from urllib.parse import urlparse

def get_path_files(path):
    file_names = []
    for root, __, files in os.walk(path):
        for file in files:
            file_names.append(os.path.join(root, file))
    return file_names

def get_image(url, filepath):
    response = requests.get(url)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    url_parsed = urlparse(url)
    return os.path.splitext(url_parsed.path)[1]
