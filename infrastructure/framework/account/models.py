from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class UserAccount(AbstractUser):
    uuid = models.UUIDField(primary_key=True)
