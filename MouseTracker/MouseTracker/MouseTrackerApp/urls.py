from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from MouseTracker.MouseTrackerApp.views import index

urlpatterns = [
    path('', index, name='index'),
]

