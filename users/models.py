from django.contrib.auth.models import AbstractUser
from django.db import models

from users.manager import CustomUserManager


class User(AbstractUser):

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def is_artist(self):
        return Artists.objects.filter(user=self).exists()

    def update_first_name(self, first_name):
        self.first_name = first_name if first_name else self.first_name

    def update_last_name(self, last_name):
        self.first_name = last_name if last_name else self.last_name

    def update_phone(self, phone):
        self.phone = phone if phone else self.phone

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'

class Artists(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, unique=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="artists")
    price_per_hour = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)
    social_links = models.JSONField(default=dict)


    def update_price_per_hour(self, new_price):
        self.price_per_hour = new_price if new_price else self.price_per_hour

    def update_availability(self, availability):
        self.availability = availability if availability else self.availability

    def update_stage_name(self, new_stage_name):
        self.stage_name = new_stage_name if new_stage_name else self.stage_name

    def update_genres(self, new_genres):
        db_genre = Genre.objects.filter(name__in=new_genres)
        self.genres.set(db_genre)

    def update_social_links(self, links):
        self.social_links.update(links)

    def __str__(self):
        return f'{self.user.username}'
