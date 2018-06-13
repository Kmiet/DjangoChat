from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'lobby'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']
        colour = text_data_json['colour']
        prev_name = text_data_json['prev']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': name,
                'colour': colour,
                'prev': prev_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        name = event['name']
        colour = event['colour']
        prev_name = event['prev']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'name': name,
            'colour': colour,
            'message': message,
            'prev': prev_name
        }))

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['channel_id']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']
        colour = text_data_json['colour']
        prev_name = text_data_json['prev']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': name,
                'colour': colour,
                'prev': prev_name
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        name = event['name']
        colour = event['colour']
        prev_name = event['prev']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'name': name,
            'colour': colour,
            'message': message,
            'prev': prev_name
        }))