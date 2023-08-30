from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_notification
from django.utils import timezone
from datetime import timedelta


@shared_task
def check_and_send_notifications():
    """Отправляет напоминание о привычке пользователю в телеграм """
    for habit in Habit.objects.all():
        chat_id = habit.user.telegram_id
        now = timezone.now()
        if now > habit.time:
            time = habit.time + timedelta(days=habit.periodicity)
        else:
            time = habit.time

        message = f'{habit.action} в {time} в {habit.place}'

        send_telegram_notification(message, chat_id)
