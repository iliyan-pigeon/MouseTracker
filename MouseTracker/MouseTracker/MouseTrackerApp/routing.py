from django.urls import re_path

from MouseTracker.MouseTrackerApp.consumers import TheConsumer

websocket_urlpatterns = (
    re_path(r'ws/socket-server', TheConsumer.as_asgi())
)
