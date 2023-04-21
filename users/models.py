from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to='users/', default='users/default/default_pic.jpg')
