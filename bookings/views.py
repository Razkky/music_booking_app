from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from utils.response import CustomResponse

from bookings.serializer import BookingSerializer
from bookings.service import BookingService


class BookEventView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def post(self, request, event_id):
        booking = BookingService.book_event(request.user, event_id)
        return CustomResponse(data=self.serializer_class(booking).data)

class ListBookingsView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get(self, request):
        bookings = BookingService.get_bookings(request.user)
        return CustomResponse(data=self.serializer_class(bookings, many=True).data)
