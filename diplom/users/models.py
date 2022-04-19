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

    def editUser(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.about = request.POST['about']
        user.email = request.POST['email']
        if request.FILES.get('avatar', False):
            user.avatar.delete(save=True)
            user.avatar = request.FILES['avatar']
        user.country = request.POST['country']
        user.city = request.POST['city']
        user.save()

    def getHosts(self, request):
        hosts = CustomUser.objects.filter(house__isnull=False)
        formData = {}
        if request.GET:
            data = request.GET
            if data['city']:
                hosts = hosts.filter(city__icontains=request.GET['city'])
            if data['country']:
                hosts = hosts.filter(country__icontains=request.GET['country'])
            if data['guestCount']:
                hosts = hosts.filter(house__guestCount__lte=request.GET['guestCount'])
            if data['gender']:
                hosts = hosts.filter(gender=request.GET['gender'])
            formData = request.GET
        return hosts, formData
