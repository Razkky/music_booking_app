#!/usr/bin/env python3

from events.serializer import EventSerializer
from rest_framework import serializers


class BookingSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    event = serializers.SerializerMethodField()
    status = serializers.CharField()
    price = serializers.IntegerField()

    def get_event(self, obj):
        return EventSerializer(obj.event).data
