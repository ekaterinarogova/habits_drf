
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Создает объект :model:`users.User` """

    serializer_class = UserSerializer
    queryset = User.objects.all()
