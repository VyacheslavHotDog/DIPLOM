from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from . import consumers
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.ChatConsumer.as_asgi())
]