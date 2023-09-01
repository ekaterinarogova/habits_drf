from django.urls import path
from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitListAPIView, HabitUpdateAPIView,
                          HabitDeleteAPIView, PublicHabitListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('list/', HabitListAPIView.as_view(), name='list-habit'),
    path('public_list/', PublicHabitListAPIView.as_view(), name='list-public-habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update-habit'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete-habit'),
 ]
