from django.db import transaction
from django.db.models import ObjectDoesNotExist

from users.models import Artists, User


class UserService:

    @staticmethod
    def create_user(**kwargs):
        is_artist = kwargs.pop("is_artist", False)
        with transaction.atomic():
            new_user = User.objects.create_user(is_active=True, **kwargs)
            if is_artist:
                ArtistService.create_artist(new_user)
        return new_user

    @staticmethod
    def update_user(user, **user_data):
        with transaction.atomic():
            UserService._update_user_profile(user, **user_data)
            ArtistService.update_profile(user, **user_data)
        return user

    @staticmethod
    def _update_user_profile(user: User, **user_data):
        user.update_first_name(user_data.get('first_name'))
        user.update_last_name(user_data.get('last_name'))
        user.update_phone(user_data.get('phone'))
        user.save()


class ArtistService:

    @staticmethod
    def create_artist(user):
        Artists.objects.create(user=user)

    @staticmethod
    def update_profile(user, **profile_data):
        try:
            artist: Artists = Artists.objects.get(user=user)
            artist.update_price_per_hour(profile_data.get('price_per_hour'))
            artist.update_availability(profile_data.get('availability'))
            ArtistService._update_genre(artist, profile_data.get('genres'))
            ArtistService._update_social_links(artist, profile_data.get('social_links'))
            artist.save()
        except Artists.DoesNotExist:
            return
    @staticmethod
    def _update_genre(artist, genres):
        artist.update_genres(genres)

    @staticmethod
    def _update_social_links(artist, social_links):
        artist.update_social_links(social_links)

    @staticmethod
    def get_all_artists():
        return User.objects.filter(artists__isnull=False).select_related(
            'artists').prefetch_related('artists__genres')

    @staticmethod
    def get_artitst(id):
        user = User.objects.filter(id=id).select_related(
            'artists').prefetch_related('artists__genres').first()
        if not user:
            raise ObjectDoesNotExist("Artists not found")
        return user
