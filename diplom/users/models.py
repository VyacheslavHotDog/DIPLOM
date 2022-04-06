from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ User """

    about = models.CharField(max_length=1000)
    age = models.IntegerField()
    gender = models.BooleanField()
    country = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images')
    city = models.CharField(max_length=50, null=True)
    vk = models.CharField(max_length=200, null=True)
    telegram = models.CharField(max_length=200, null=True)
