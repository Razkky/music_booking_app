from rest_framework import serializers
from users.models import Artists


class CreateEventSerializer(serializers.Serializer):

    name = serializers.CharField()
    description = serializers.CharField()
    artist_ids = serializers.ListField()
    location = serializers.CharField()
    date = serializers.DateTimeField()
    price = serializers.IntegerField()

    def validate_artists(self, artist_ids):
        existing_artist_ids = set(
            Artists.objects.filter(id__in=artist_ids).values_list("id", flat=True)
        )

        invalid_ids = [artist_id for artist_id in artist_ids if artist_id not in existing_artist_ids]

        if invalid_ids:
            raise serializers.ValidationError(
                f"Artist with IDs {invalid_ids} does not exist."
            )

        return artist_ids

class UpdateEventSerializer(serializers.Serializer):

    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    location = serializers.CharField(required=False)


class EventSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    artists = serializers.SerializerMethodField()
    location = serializers.CharField()
    date = serializers.DateTimeField()
    price = serializers.IntegerField()

    def get_artists(self, obj):
        return [artist.user.first_name for artist in obj.artists.all()]
