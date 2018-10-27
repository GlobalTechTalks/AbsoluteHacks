from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    date_of_birth = models.DateField(verbose_name="DOB")
    college = models.CharField(max_length=120)
