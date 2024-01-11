from django.urls import re_path

from MouseTracker.MouseTrackerApp.consumers import MouseConsumer

websocket_urlpatterns = (
    re_path(r'ws/mouse/$', MouseConsumer.as_asgi())
)
