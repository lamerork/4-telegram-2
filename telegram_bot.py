import telegram
import argparse
from environs import Env
import random
from main_functions import get_path_files


def upload_image_to_telegram(token, chat_name, file_name):
    
    bot = telegram.Bot(token = token)
    with open(file_name, "rb") as file:
        bot.send_photo(chat_id = chat_name, photo = file, timeout = 300)

def main():

    env = Env()
    env.read_env()

    parser = argparse.ArgumentParser(description="Бот публикует картинки в телеграм канал")
    parser.add_argument("-p", help="Путь к картинке", default=random.choice(get_path_files(env.str('DIRECTORY'))))
    args = parser.parse_args()

  
    file_name = args.p

    upload_image_to_telegram(env.str('TELEGRAM_TOKEN'), env.str('CHAT_NAME'), file_name)

if __name__ == "__main__":

    main()