from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('Email address', unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField("Phone number", max_length=13)
    image = models.ImageField('Image', upload_to='users/',blank=True, null=True)
    bio = models.CharField("Bio", max_length=255, blank=True, null=True)