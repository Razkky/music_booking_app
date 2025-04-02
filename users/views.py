from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from utils.response import CustomResponse

from users.serializer import (CustomTokenObtainPairSerializer,
                              UpdateUserSerializer, UserSerializer)
from users.service import ArtistService, UserService


class CustomObtainTokenPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        return CustomResponse(data=serialized_data.validated_data, status=status.HTTP_200_OK)



class CreateUserView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        user = UserService.create_user(**serialized_data.validated_data)
        user = self.serializer_class(user).data
        return CustomResponse(data=user)

class UpdateUserView(generics.GenericAPIView):

    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        user = UserService.update_user(request.user, **serialized_data.validated_data)
        return CustomResponse(data=UserSerializer(user).data)

class ListArtistsView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        artits = ArtistService.get_all_artists()
        return CustomResponse(data=self.serializer_class(artits, many=True).data)

class PreviewArtistView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request, id=None):
        artist = ArtistService.get_artitst(id)
        return CustomResponse(data=self.serializer_class(artist).data)
