# Generated by Django 4.2.4 on 2023-08-28 06:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='место')),
                ('time', models.DateTimeField(verbose_name='время')),
                ('action', models.CharField(max_length=200, verbose_name='действие')),
                ('is_pleasant', models.BooleanField(default=False, verbose_name='приятная привычка')),
                ('reward', models.CharField(blank=True, max_length=200, null=True, verbose_name='вознаграждение')),
                ('realization_time', models.PositiveSmallIntegerField(help_text='время на выполнение в секундах', validators=[django.core.validators.MaxValueValidator(limit_value=120)], verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная привычка')),
                ('periodicity', models.PositiveSmallIntegerField(default=1, help_text='периодичность выполнения в днях', validators=[django.core.validators.MaxValueValidator(limit_value=7)], verbose_name='периодичность')),
                ('connected_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
