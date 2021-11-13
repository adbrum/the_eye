from rest_framework import serializers
from events.models import Event, Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('session_id', 'timestamp', 'data', 'name', 'category')
