from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериалайзер для класса :model:`habits.Habit`"""
    connected_habit = serializers.PrimaryKeyRelatedField(queryset=Habit.objects.filter(is_pleasant=True),
                                                        default=None)

    def validate(self, attrs):
        if self.initial_data.get('reward') is not None and self.initial_data.get('connected_habit') is not None:
            raise serializers.ValidationError('У привычки не может быть одновременно вознаграждения и связанной привычки')
        if self.initial_data.get('is_pleasant'):
            if self.initial_data.get('connected_habit') is not None or self.initial_data.get('reward') is not None:
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
        return attrs

    class Meta:
        model = Habit
        fields = ('__all__')

