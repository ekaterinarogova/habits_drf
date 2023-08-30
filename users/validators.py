from rest_framework import serializers


def check_telegram_id(value):
    if not value.isdigit():
        raise serializers.ValidationError('Telegram id должно состоять только из чисел')
