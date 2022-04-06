"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from base.views import *
from users.views import *
import debug_toolbar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  path('', main, name='main'),
                  path('admin/', admin.site.urls),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('signup', SignUpView.as_view(), name='signup'),

                  path('messages', messages, name='messages'),
                  path('trips/<int:trip_id>/', trip, name='trip'),
                  path('profile', profile, name='profile'),
                  path('hosts', hosts, name='hosts'),
                  path('trips', trips, name='trips'),
                  path('hosts/<int:host_id>/', host, name='host'),

                  path('firstMessage', firstMessage, name='firstMessage'),
                  path('profile/add_house', addHouse, name='addHouse'),
                  path('profile/deleteTrip', deleteTrip, name='deleteTrip'),
                  path('profile/deleteHouse', deleteHouse, name='deleteHouse'),
                  path('profile/deleteHouseImage', deleteHouseImage, name='deleteHouseImage'),
                  path('profile/editTrip', editTrip, name='editTrip'),
                  path('profile/editHouse', editHouse, name='editHouse'),
                  path('addtrip', addtrip, name='addtrip'),
                  path('messages/ajax', load_messages, name='load_messages'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
