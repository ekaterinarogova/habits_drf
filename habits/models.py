from django.db import models
from django.core.validators import MaxValueValidator

from django.conf import settings


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             related_name='habit', null=True)
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.DateTimeField(verbose_name='время')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    connected_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка',
                                        null=True, blank=True)
    reward = models.CharField(max_length=200, verbose_name='вознаграждение', null=True, blank=True)
    realization_time = models.PositiveSmallIntegerField(verbose_name='время на выполнение',
                                                        help_text='время на выполнение в секундах',
                                                        validators=[MaxValueValidator(limit_value=120)])
    is_public = models.BooleanField(verbose_name='публичная привычка', default=False)
    periodicity = models.PositiveSmallIntegerField(verbose_name='периодичность', default=1,
                                                   help_text='периодичность выполнения в днях',
                                                   validators=[MaxValueValidator(limit_value=7)])

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


