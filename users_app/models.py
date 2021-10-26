from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Person(AbstractUser):
    email = models.EmailField(max_length=128, unique=True)
    surname = models.CharField(max_length=128, blank=True,)
    avatar = models.ImageField(upload_to='Person_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    rate = models.ImageField(default=0, blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def __str__(self):
        return self.username

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
