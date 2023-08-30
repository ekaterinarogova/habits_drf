from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_id = models.CharField(max_length=150, verbose_name='имя в телеграм')
