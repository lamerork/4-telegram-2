# Телеграм бот отправки фотографий космоса в телеграм канал

Бот постит фотографии SpaceX, NASA в телеграм канал

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как настроить

В файле ```.env``` должны быть переменные

```
NASA_TOKEN = Токен NASA
TELEGRAM_TOKEN = Токен Телеграм бота
CHAT_NAME = Имя канала в телеграм
INTERVAL = Время через которое бот опубликует фотографию в секундах
DIRECTORY = Директория картинок
```

### Как использовать

Скачиваем фотографии последнего запуска ракет SpaceX
```python fetch_spacex_last_launсh.py```

Скачать фотографии можно по ID запуска ракеты
```python fetch_spacex_last_launсh.py -s 'ID Запуска'``` 

Скачиваем 50 фотографий NASA APOD
 ```python fetch_nasa_apod.py```

Скачиваем последнии фотографии земли NASA EPIC
```python fetch_nasa_epic.py```

Публикуем случайное фотографию в Телеграм канал
```python telegram_bot.py```

Публикуем фотографию в Телеграм канал
```python telegram_bot.py -p 'Путь к фотографии'```

Публикуем случайные фотографии каждые 4 часа 
```python send_images.py```

Публикуем случайные фотографии указанное время в секуднах
```python send_images.py -s 'секунды'``` 
