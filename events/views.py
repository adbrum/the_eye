from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from events.serializers import EventSerializer, SessionSerializer
from .models import Event, Session


class SessionModelViewSet(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class EventList(APIView):
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

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
