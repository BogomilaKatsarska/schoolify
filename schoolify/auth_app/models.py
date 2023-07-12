from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from schoolify.auth_app.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    personal_number = models.PositiveIntegerField(
        unique=True,
        null=False,
        blank=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )
    USERNAME_FIELD = 'personal_number'
    objects = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=35,
    )
    last_name = models.CharField(
        max_length=35,
    )
    school_grade = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
