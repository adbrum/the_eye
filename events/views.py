from rest_framework.generics import ListCreateAPIView

from events.serializers import SessionSerializer
from .models import Session


class SessionModelViewSet(ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
