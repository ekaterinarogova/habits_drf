# Generated by Django 4.2.4 on 2023-08-28 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
