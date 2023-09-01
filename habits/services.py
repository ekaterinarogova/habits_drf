import requests

from django.conf import settings


def send_telegram_notification(message, chat_id):
    """Отправляет напоминание пользователю в телеграм"""
    url = f'https://api.telegram.org/bot{settings.TELEGRAM_API_KEY}/sendMessage?chat_id={chat_id}&text={message}"'
    try:
        requests.post(url=url)
    except requests.exceptions.RequestException as e:
        print(e)

