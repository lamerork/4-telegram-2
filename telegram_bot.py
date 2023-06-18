import os
import telegram
import argparse
from environs import Env
import random
from main_functions import get_path_files


def upload_image_to_telegram(token, chat_name, files):
    
    bot = telegram.Bot(token = token)
    bot.send_photo(chat_id = chat_name, photo = open(files, "rb"), timeout = 300)

def main():

    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description="Бот публикует картинки в телеграм канал")
    parser.add_argument("-p", help="Путь к картинке")
    args = parser.parse_args()

    if args.p: 
        file = args.p
    else: 
        file = random.choice(get_path_files(env.str('DIRECTORY')))

    upload_image_to_telegram(env.str('TELEGRAM_TOKEN'), env.str('CHAT_NAME'), file)

if __name__ == "__main__":

    main()