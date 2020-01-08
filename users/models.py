from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    is_studentt = models.BooleanField(null=True)
    is_instructor = models.BooleanField(null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.name)