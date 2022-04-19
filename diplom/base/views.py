from django.core.exceptions import *
from django.shortcuts import render, redirect
from .forms import *
from django.conf import settings
from users.models import CustomUser
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers


def main(request):
    trips = Trip.objects.all()
    return render(request, "main/main.html", {'trips': trips, 'MEDIA_URL': settings.MEDIA_URL[1:]})


def hosts(request):
    hosts, formData = CustomUser().getHosts(request)
    return render(request, "hosts/hosts.html",
                  {'hosts': hosts, 'formData': formData, 'MEDIA_URL': settings.MEDIA_URL[1:]})


def trips(request):
    trips, formData = Trip().getTrips(request)
    tripsCount = len(trips)
    return render(request, "trips/trips.html",
                  {'trips': trips, 'tripsCount': tripsCount, 'formData': formData, 'MEDIA_URL': settings.MEDIA_URL[1:]})


def messages(request):
    userId = request.user.id
    messages = Message.objects.filter(Q(author=userId) | Q(receiver=userId)).order_by('receiver', 'date')
    receiverIds = []
    for message in messages:
        if message.receiver not in receiverIds:
            receiverIds.append(message.receiver)
        if message.author not in receiverIds:
            receiverIds.append(message.author)
    if receiverIds:
        receiverIds.remove(request.user)
    return render(request, 'chat/chat.html', {'messages': messages, 'users': receiverIds})


def load_messages(request):
    """Загрузка сообщений"""
    userId = request.GET.get('userId', None)
    messages = Message.objects.filter(
        Q(author=request.user.id, receiver=userId) | Q(author=userId, receiver=request.user.id)).order_by('date')
    leads_as_json = serializers.serialize('json', messages)
    response = {
        'msg': leads_as_json
    }
    return JsonResponse(response)


def profile(request):
    if request.method == 'POST':
        CustomUser().editUser(request)
        return redirect('profile')
    trips = Trip.objects.filter(userId=request.user.id)
    try:
        house = request.user.house
    except ObjectDoesNotExist:
        house = None
    return render(request, 'profile.html', {'trips': trips, 'house': house, 'MEDIA_URL': settings.MEDIA_URL[1:]})


def trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/trip.html', {'trip': trip})


def host(request, host_id):
    host = CustomUser.objects.get(id=host_id)
    return render(request, 'hosts/host.html', {'host': host})


def addtrip(request):
    """ Добавить путешествие """
    if request.method == 'POST':
        inst = Trip(userId=request.user)
        form = AddTripForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = AddTripForm()
    return render(request, 'trips/addtrip.html', {'form': form})


def deleteTrip(request):
    trip = Trip.objects.get(id=request.GET.get('tripId'))
    trip.delete()
    return redirect('profile')


def addHouse(request):
    if request.method == 'POST':
        House().addHouse(request)
        return redirect('profile')
    return render(request, 'hosts/addHouse.html')


def deleteHouse(request):
    house = House.objects.get(id=request.GET.get('houseId'))
    house.delete()
    return redirect('profile')


def firstMessage(request):
    if request.method == 'POST':
        data = request.POST
        receiver = CustomUser.objects.get(id=request.POST['receiver'])
        Message.objects.create(content=data['content'], author=request.user, receiver=receiver)
    return redirect('/hosts/{}'.format(data['receiver']))


def editTrip(request):
    if request.method == 'POST':
        inst = Trip.objects.get(userId=request.user)
        form = AddTripForm(request.POST, request.FILES, instance=inst)
        if form.is_valid():
            form.save()
            return redirect('editTrip')
    else:
        return render(request, 'trips/editTrip.html')


def editHouse(request):
    if request.method == 'POST':
        House().editHouse(request)
        return redirect('editHouse')
    else:
        return render(request, 'hosts/editHouse.html')


def deleteHouseImage(request):
    image = HouseImages.objects.get(id=request.POST['imageId'])
    image.delete()
    return redirect('editHouse')
