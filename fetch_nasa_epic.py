from dotenv import load_dotenv
import os
import requests
from datetime import datetime
from main_functions import get_image


def fetch_nasa_epic(token):

    payload = {
        "api_key": token,
    }

    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params = payload)
    response.raise_for_status()
    nasa_json = response.json()


    for i, nasa in enumerate(nasa_json):

        image = nasa["image"]
        data =  datetime.strptime(nasa["identifier"], "%Y%m%d%H%M%S")
        url = f"https://epic.gsfc.nasa.gov/archive/natural/{data:%Y/%m/%d}/png/{image}.png"
        file_name = f"images/epic_{i}.png"
        
        get_image(url, file_name)


def main():
    load_dotenv()
    fetch_nasa_epic(os.environ["NASA_TOKEN"])


if __name__ == "__main__":
    main()