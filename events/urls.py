from django.urls import path

from .views import SessionModelViewSet


urlpatterns = [
    path('sessions/', SessionModelViewSet.as_view(), name='session'),
]
