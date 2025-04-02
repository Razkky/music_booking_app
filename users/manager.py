
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, **kwargs):
        if not email:
            raise ValueError("User must have a valid email address")
        password = kwargs.get('password')
        if not password:
            raise ValueError("User must have a password")
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **kwargs)
        print("Creating user")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('password', password)
        self.create_user(email, **kwargs)
