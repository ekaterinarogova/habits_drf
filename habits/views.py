from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitListPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создает объект :model:`habits.Habit`"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """Выводит список объектов :model:`habits.Habit`"""
    serializer_class = HabitSerializer
    pagination_class = HabitListPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Получает список объектов созданных текущим пользователем"""
        user = self.request.user
        queryset = Habit.objects.filter(user=user)
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    """Выводит список объектов с флагом is_public модели :model:`habits.Habit`"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitListPaginator
    permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирует объект :model:`habits.Habit`"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Удаляет объект :model:`habits.Habit`"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
