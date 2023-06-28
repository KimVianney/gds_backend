from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


from .manager import CustomUserManager


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.URLField(default='', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        db_table = 'gds_users'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def update(self, data):
        for field in ['first_name', 'last_name', 'avatar']:
            if field in data:
                setattr(self, field, data[field])
            self.save()
            return self

    @property
    def get_access_token(self):
        token = RefreshToken.for_user(self)
        return {
            'access_token': str(token.access_token),
        }


