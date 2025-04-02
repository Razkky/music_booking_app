#!/usr/bin/env python3


from events.service import EventService

from bookings.models import Booking


class BookingService:

    @staticmethod
    def book_event(user, event_id):
        event = EventService.get_event_by_id(event_id)
        booking = BookingService._create_new_booking(user, event)
        return booking

    @staticmethod
    def _create_new_booking(user, event):
        booking =Booking.objects.create(user=user, event=event)
        return booking

    @staticmethod
    def get_bookings(user):
        return Booking.objects.filter(user=user).all()
