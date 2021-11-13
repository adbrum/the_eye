from django.urls import path

from .views import ErrorModelViewSet, EventDetail, EventList, SessionModelViewSet


urlpatterns = [
    path('sessions/', SessionModelViewSet.as_view(), name='session'),
    path('events/', EventList.as_view(), name='event'),
    path('event_detail/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('errors/', ErrorModelViewSet, name='error'),
]
