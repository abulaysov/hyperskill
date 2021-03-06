from django.db import models
from django.contrib.auth.models import User


class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
