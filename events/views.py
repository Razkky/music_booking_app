from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from utils.response import CustomResponse

from events.serializer import (CreateEventSerializer, EventSerializer,
                               UpdateEventSerializer)
from events.service import EventService


class CreateEventView(generics.GenericAPIView):

    serializer_class = CreateEventSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        event = EventService.create_event(request.user, **serialized_data.validated_data)
        return CustomResponse(data=EventSerializer(event).data)

class UpdateEventView(generics.GenericAPIView):

    serializer_class = UpdateEventSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        event = EventService.update_event(id, request.user, **serialized_data.validated_data)
        return CustomResponse(data=EventSerializer(event).data)

class ListEventView(generics.GenericAPIView):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        events = EventService.get_all_events()
        return CustomResponse(data=self.serializer_class(events, many=True).data)
