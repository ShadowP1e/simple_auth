from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # переделываем стандартный класс User
    status = models.CharField(max_length=200)
