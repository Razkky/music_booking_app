
from django.urls import path

from users import views

urlpatterns = [
    path("", views.CreateUserView.as_view(), name="register-user"),
    path("<int:id>", views.PreviewArtistView.as_view(), name="register-user"),
    path("update", views.UpdateUserView.as_view(), name="update-user"),
    path("auth/login", views.CustomObtainTokenPairView.as_view(), name="login"),
    path('artits/all', views.ListArtistsView.as_view(), name='list-artist'),
]
