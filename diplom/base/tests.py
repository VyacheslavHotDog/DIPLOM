from django.test import TestCase

# Create your tests here.

from .models import Trip, House
from users.models import CustomUser


class TripModelTest(TestCase):
    fixtures = ['dump.json', ]

    def test_create_trip(self):
        Trip.objects.create(id=1000, header='tripCreate', searchingGender=1, searchingAge=1,
                            description='tripCreate',
                            dateEnd='2000-06-02', dateBegin='2000-06-02', country='russia', category=1,
                            userId=CustomUser.objects.get(id=1))
        trip = Trip.objects.get(id=1000)
        self.assertEquals(trip.header, 'tripCreate')

    def test_edit_trip(self):
        trip = Trip.objects.get(id=1)
        trip.header = 'editedTrip'
        trip.save()
        newTrip = Trip.objects.get(id=1)
        self.assertEquals(newTrip.header, 'editedTrip')

    def test_create_host(self):
        House.objects.create(id=1000, address='testAdress', description='testDescription', guestCount=2,
                                     userId=CustomUser.objects.get(id=1))
        house = House.objects.get(id=1000)
        self.assertEquals(house.address, 'testAdress')

    # def test_edit_host(self):
    #     house = House.objects.get(id=1)
    #     self.assertEquals(house.address, 'trip1')

    #
    # def test_date_of_death_label(self):
    #     author=Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEquals(field_label,'died')
    #
    # def test_first_name_max_length(self):
    #     author=Author.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEquals(max_length,100)
    #
    # def test_object_name_is_last_name_comma_first_name(self):
    #     author=Author.objects.get(id=1)
    #     expected_object_name = '%s, %s' % (author.last_name, author.first_name)
    #     self.assertEquals(expected_object_name,str(author))
    #
    # def test_get_absolute_url(self):
    #     author=Author.objects.get(id=1)
    #     #This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')
