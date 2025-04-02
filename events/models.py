from django.db import models
from users.models import Artists, User


class Event(models.Model):

    organizer = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="events"
    )
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    artists = models.ManyToManyField(Artists)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    price = models.IntegerField(default=0) # Store in kobo


    def update_artists(self, artits_id):
        artists = Artists.objects.filter(id__in=artits_id)
        self.artists.set(artists)

    def update_price(self, new_price):
        self.price = new_price if new_price else self.price

    def update_location(self, new_location):
        self.location = new_location if new_location else self.location

    def update_name(self, new_name):
        self.name = new_name if new_name else self.name

    def update_description(self, new_description):
        self.description = new_description if new_description else self.description


    def __str__(self):
        return f'{self.organizer.first_name} events'
