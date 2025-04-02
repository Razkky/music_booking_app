#!/usr/bin/env python3


from django.urls import path

from events import views

urlpatterns = [
    path('', views.CreateEventView.as_view(), name="create-event"),
    path('update/<int:id>', views.UpdateEventView.as_view(), name="update-event"),
    path('all', views.ListEventView.as_view(), name="list-events"),
]
