from django.contrib.auth import get_user_model
from django.db import models

from todoApi.todos.choices import TodoStateChoices

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Todo(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    category = models.ForeignKey(
        to=Category,
        related_name='todos',
        on_delete=models.CASCADE,
    )
    state = models.BooleanField(
        choices=[
            (True, TodoStateChoices.DONE),
            (False, TodoStateChoices.NOT_DONE)
        ],
        default=False,
    )
    assignees = models.ManyToManyField(
        to=UserModel,
        related_name='todos',
        blank=True,
    )
