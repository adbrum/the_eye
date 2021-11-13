from django.urls import path

from .views import EventList, SessionModelViewSet


urlpatterns = [
    path('sessions/', SessionModelViewSet.as_view(), name='session'),
    path('events/', EventList.as_view(), name='event'),
]
