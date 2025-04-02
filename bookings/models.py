
from django.db import models
from events.models import Event
from users.models import User


class Booking(models.Model):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = (
        (STATUS_PENDING, STATUS_PENDING),
        (STATUS_CONFIRMED, STATUS_CONFIRMED),
        (STATUS_CANCELLED, STATUS_CANCELLED),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)  # Store in kobo
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING
    )


    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.event.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.event.name} - {self.status}"
