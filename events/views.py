from django.core.exceptions import SuspiciousFileOperation
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from events.serializers import ErrorSerializer, EventSerializer, SessionSerializer
from events.task import create_task
from .models import Error, Event, Session


class SessionModelViewSet(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class EventList(ListCreateAPIView):
    def get(self, request, format=None):
        if request.GET.get('category'):
            events = Event.objects.filter(
                category=request.GET.get('category'))
        elif request.GET.get('session_id'):
            events = Event.objects.filter(
                session_id=request.GET.get('session_id'))
        elif request.GET.get('name'):
            events = Event.objects.filter(
                name=request.GET.get('name'))
        elif request.GET.get('timestamp'):
            events = Event.objects.filter(
                timestamp__gte=request.GET.get('timestamp'))
        else:
            events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def create(self, request, format=None):
        serializer = create_task(request.data)
        if serializer.status_code == 201:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventSerializer(events)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = EventSerializer(events, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ErrorModelViewSet(ReadOnlyModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
