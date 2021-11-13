from celery import shared_task
from rest_framework import status
from rest_framework.response import Response
from events.models import Event
from rest_framework import serializers
from events.serializers import EventSerializer

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@shared_task()
def create_task(serializer):
    serializer.save()
