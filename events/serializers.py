from rest_framework import serializers
from events.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id',)
