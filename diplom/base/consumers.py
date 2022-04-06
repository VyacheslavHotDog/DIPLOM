import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from . models import *
from users.models import CustomUser


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def save_message(self, author, receiver, content):
        Message.objects.create(author=author, receiver=receiver, content=content)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        content = text_data_json['content']
        author = CustomUser.objects.get(id=int(text_data_json['author']))
        receiver = CustomUser.objects.get(id=int(text_data_json['receiver']))
        self.save_message(author, receiver, content)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'content': text_data_json['content'],
                'author': text_data_json['author'],
                'receiver': text_data_json['receiver'],
            }
        )

    def chat_message(self, event):

        self.send(text_data=json.dumps({
            'type': 'chat',
            'content': event['content'],
            'author': int(event['author']),
            'receiver': int(event['receiver']),
        }))
