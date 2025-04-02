
from django.urls import path

from bookings import views

urlpatterns = [
    path('<int:event_id>', views.BookEventView.as_view(), name='book-event'),
    path('all', views.ListBookingsView.as_view(), name='list-booking')
]
