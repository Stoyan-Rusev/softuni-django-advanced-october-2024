from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'py', 'Python'
    JAVASCRIPT = 'js', 'Javascript'
    JAVA = 'j', 'Java'
    C = "c", "C"
    CPLUSPLUS = 'cpp', 'C++'
    CSHARP = 'cs', 'C#'
    OTHER = 'other', 'Other'
