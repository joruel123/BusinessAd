from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_approve = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
