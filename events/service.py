from django.db.models import ObjectDoesNotExist

from events.models import Event


class EventService:

    @staticmethod
    def create_event(user, **event_data):
        artist_ids = event_data.pop('artist_ids', [])
        event: Event = Event.objects.create(organizer=user, **event_data)
        event.update_artists(artist_ids)
        return event


    @staticmethod
    def update_event(event_id, **event_data):
        event: Event = EventService.get_event_by_id(event_id)
        EventService._update_event_data(event, **event_data)
        return event

    @staticmethod
    def _update_event_data(event, **event_data):
        event.update_price(event_data.get('price', 0))
        event.update_description(event_data.get('description', ''))
        event.update_name(event_data.get('name', ''))
        event.update_location(event_data.get('location', ''))
        event.save()

    @staticmethod
    def get_all_events():
        events =  Event.objects.prefetch_related('artists').all()
        return events

    @staticmethod
    def get_event_by_id(event_id):
        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise ObjectDoesNotExist(f'Event not found for this {event_id}')
