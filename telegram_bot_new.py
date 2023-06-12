import os
import time
import telegram
from dotenv import load_dotenv


def upload_images_to_telegram(token, chat_name, update_period):
    
    bot = telegram.Bot(token = token)
    
    for file in os.listdir(f"images"):
        with open(f"images/{file}", "rb") as photo:
            bot.send_photo(
                chat_id = chat_name,
                photo = photo,
                timeout = 30
            )
            time.sleep(update_period)


def main():
    load_dotenv()
    update_period = 15
    upload_images_to_telegram(os.environ["TELEGRAM_TOKEN"], os.environ["CHAT_NAME"], update_period)

if __name__ == "__main__":
    main()