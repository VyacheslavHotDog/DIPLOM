from django.db import models
from users.models import CustomUser


class Trip(models.Model):
    """ Путешествие """
    header = models.CharField(max_length=100, null=True)
    searchingGender = models.IntegerField(null=True)
    searchingAge = models.IntegerField(null=True)
    description = models.CharField(max_length=1000)
    dateEnd = models.DateField()
    dateBegin = models.DateField()
    country = models.CharField(max_length=100)
    category = models.IntegerField()
    logo = models.ImageField(upload_to='images', null=True)
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def getTrips(self, request):
        age_table = [[0, 25], [25, 40], [40, 100]]
        trips = Trip.objects.all()
        data = {}
        if request.GET:
            data = request.GET
            if data['country']:
                trips = trips.filter(country__icontains=data['country'])
            if data['category']:
                trips = trips.filter(category=data['category'])
            if data['gender']:
                trips = trips.filter(userId__gender=data['gender'])
            if data['age']:
                trips = trips.filter(userId__age__gte=age_table[int(data['age'])][0],
                                     userId__age__lte=age_table[int(data['age'])][1])
        return trips, data


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
    userId = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def addHouse(self, request):
        data = request.POST
        house = House.objects.create(address=data['address'], description=data['description'],
                                     guestCount=data['guestCount'], userId=request.user)
        for i in range(3):
            if request.FILES.get('img{}'.format(i), False):
                HouseImages.objects.create(house=house, image=request.FILES['img{}'.format(i)])

    def editHouse(self, request):
        data = request.POST
        house = House.objects.get(userId=request.user)
        house.address = data['address']
        house.description = data['description']
        house.guestCount = data['guestCount']
        for i in range(3):
            if request.FILES.get('img{}'.format(i), False):
                HouseImages.objects.create(house=house, image=request.FILES['img{}'.format(i)])
        house.save()


class HouseImages(models.Model):
    """ Изображения """
    image = models.ImageField(upload_to='images')
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Review(models.Model):
    text = models
