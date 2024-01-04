from django.urls import path

from MouseTracker.MouseTrackerApp.views import index

urlpatterns = [
    path('', index, name='index'),
]
