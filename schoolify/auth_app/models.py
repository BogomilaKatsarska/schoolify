from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator
from django.db import models
from schoolify.auth_app.managers import AppUserManager
from schoolify.auth_app.validators import validate_len_personal_number, validate_school_year_range, \
    validate_capitalized


class AppUser(AbstractBaseUser, PermissionsMixin):
    MAX_PERSONAL_NUMBER = 9912319999
    personal_number = models.BigIntegerField(
        unique=True,
        validators=(
            validate_len_personal_number,
            MaxValueValidator(MAX_PERSONAL_NUMBER),
        ),
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

    def __str__(self):
        return str(self.personal_number)


class Profile(models.Model):
    first_name = models.CharField(
        validators=(validate_capitalized,),
        max_length=35,
    )
    last_name = models.CharField(
        validators=(validate_capitalized,),
        max_length=35,
    )
    school_grade = models.PositiveIntegerField(
        validators=(validate_school_year_range,),
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user} - {self.first_name} {self.last_name}'

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None
