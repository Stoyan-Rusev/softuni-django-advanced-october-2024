# Generated by Django 5.1.7 on 2025-03-25 21:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='assignees',
            field=models.ManyToManyField(blank=True, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
    ]
