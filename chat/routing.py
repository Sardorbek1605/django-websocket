from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('ws/chat/<room_name>/', consumer.Consumer.as_asgi()),
]
