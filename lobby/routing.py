from django.urls import path, include
from . import consumers

websocket_urlpatterns = [
    path('ws/lobby/', consumers.LobbyConsumer),
    path('ws/channel/<int:channel_id>/', consumers.ChatConsumer)
]