
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserSerializer(self.user).data
        return data


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(required=False)
    username = serializers.CharField()
    is_artist = serializers.BooleanField(required=False, write_only=True)

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    stage_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    availability = serializers.BooleanField(required=False, default=True)
    price_per_hour = serializers.IntegerField(required=False)
    social_links = serializers.JSONField(required=False)
    genres = serializers.ListField(child=serializers.CharField(), required=False)


class ArtistSerilizer(serializers.Serializer):

    id = serializers.IntegerField()
    user = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    price_per_hour = serializers.IntegerField()
    availability = serializers.BooleanField()

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_user(self, obj):
        return UserSerializer(obj.user).data

class ArtistDetailSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    user = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()
    price_per_hour = serializers.IntegerField()
    availability = serializers.BooleanField()
    social_links = serializers.JSONField()

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_user(self, obj):
        return UserSerializer(obj.user).data
