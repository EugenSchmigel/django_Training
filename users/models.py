from django.contrib.auth.models import AbstractUser
from django.db import models

from main.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-Mail')

    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    avatar = models.ImageField(upload_to='user/', verbose_name='Avatar', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

