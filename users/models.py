from django.db import models
from django.contrib.auth.models import AbstractUser


class UserData(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username