from rest_framework import serializers
from events.models import Error, Event, Session
from django.utils import timezone


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id',)


class EventSerializer(serializers.ModelSerializer):
    msg = ['The data can\'t be empty.',
           'The data content must a JSON format.',
           'The timestamp can\'t be greater than now.']

    def validate_data(self, data):
        if not data:
            message = self.msg[0]
            Error.objects.create(message=message)
            raise serializers.ValidationError(message)
        elif not type(data) == dict:
            message = self.msg[1]
            Error.objects.create(message=message, data=data)
            raise serializers.ValidationError(
                self.msg[1])
        return data

    def validate_timestamp(self, timestamp):
        if timestamp > timezone.now():
            message = self.msg[2]
            Error.objects.create(
                message=message, data=self.initial_data.get('data'))
            raise serializers.ValidationError(message)
        return timestamp

    class Meta:
        model = Event
        fields = ('id', 'session_id', 'timestamp', 'data', 'name', 'category')


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = '__all__'
