from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('Provide an email address')
        if not username:
            raise  ValueError('Provide a username')
        if not password:
            raise ValueError('Provide a password')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.username = username
        user.save()
        return user

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(max_length=320, unique=True)
    username = models.CharField(max_length=20, unique=True)
    avatar = models.CharField(max_length=32, default='avatar/__default.png')
    colour = models.CharField(max_length=7, default='#000000')
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

