from django.db import models
from users.models import CustomUser


class Trip(models.Model):
    """ Путешествие """
    header = models.CharField(max_length=100, null=True)
    searchingGender = models.IntegerField(max_length=10, null=True)
    searchingAge = models.IntegerField(null=True)
    description = models.CharField(max_length=1000)
    dateEnd = models.DateField()
    dateBegin = models.DateField()
    country = models.CharField(max_length=100)
    category = models.IntegerField(max_length=100)
    logo = models.ImageField(upload_to='images')
    userId = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Message(models.Model):
    """ Путешествие """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author', null=True)
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver', null=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class House(models.Model):
    """ Жилище """
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    guestCount = models.IntegerField()
    userId = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class HouseImages(models.Model):
    """ Изображения """
    image = models.ImageField(upload_to='images')
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Review(models.Model):
    text = models
