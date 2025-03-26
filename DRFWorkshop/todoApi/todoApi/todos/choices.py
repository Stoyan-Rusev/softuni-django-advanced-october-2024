from django.db import models


class TodoStateChoices(models.TextChoices):
    DONE = 'done', 'Done'
    NOT_DONE = 'not done', 'Not Done'

