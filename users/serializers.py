from rest_framework import serializers

from users.models import User
from users.validators import check_telegram_id


class UserSerializer(serializers.ModelSerializer):
    """ Сериалайзер для класса :model:`users.User`"""
    telegram_id = serializers.CharField(validators=[check_telegram_id])

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'telegram_id',)
