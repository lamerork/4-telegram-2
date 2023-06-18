import argparse
from environs import Env
import random
import time
from main_functions import get_path_files
from telegram_bot import upload_image_to_telegram


def main():
    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description="Бот публикует картинки в телеграм канал")
    parser.add_argument("-s", help="Интервал в секундах", default=env.int('INTERVAL'))
    args = parser.parse_args()


    interval = int(args.s)

    files = get_path_files(env.str('DIRECTORY'))

    while True:

        random.shuffle(files)
        for file in files:
            upload_image_to_telegram(env.str('TELEGRAM_TOKEN'), env.str('CHAT_NAME'), file)
            time.sleep(interval)

if __name__ == "__main__":

    main()