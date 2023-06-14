import os
import time
import telegram
import argparse
from environs import Env
import random


def upload_images_to_telegram(token, chat_name, files, interval):
    
    bot = telegram.Bot(token = token)
    
    for file in files:
        
        bot.send_photo(
            chat_id = chat_name,
            photo = open(file, "rb"),
            timeout = 300
        )

        time.sleep(interval)


def main():

    env = Env()
    env.read_env()

    namefiles = []

    parser = argparse.ArgumentParser(description="Бот публикует картинки в телеграм канал раз в интервал")
    parser.add_argument("-s", help="Интервал в секундах")
    args = parser.parse_args()

    if args.s: 
        interval = int(args.s)
    else: 
        interval = env.int('INTERVAL')
    

    for root, __, files in os.walk(env.str('DIRECTORY')):
        for file in files:
            namefiles.append(os.path.join(root, file))
    print(namefiles)
  
    while True:
        random.shuffle(files)
        upload_images_to_telegram(env.str('TELEGRAM_TOKEN'), env.str('CHAT_NAME'), namefiles, interval)

if __name__ == "__main__":

    main()