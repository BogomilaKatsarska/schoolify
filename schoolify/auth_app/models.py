from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from schoolify.auth_app.managers import AppUserManager
from schoolify.auth_app.validators import validate_len_personal_number, validate_school_year_range, \
    image_size_validator_10mb, validate_capitalized


class AppUser(AbstractBaseUser, PermissionsMixin):
    #TODO:EDIT BELOW: MAX_PERSONAL_NUMBER = 9999999999
    personal_number = models.PositiveIntegerField(
        unique=True,
        validators=(
            validate_len_personal_number,
            # MaxValueValidator(MAX_PERSONAL_NUMBER),
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

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return None

'''
superuser:
1999999998
123qwe!@#
teacher:
1000000001
normal:
1111100000
'''
