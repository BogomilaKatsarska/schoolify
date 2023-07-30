from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from schoolify.auth_app.managers import AppUserManager
from schoolify.auth_app.validators import validate_len_personal_number


#1:49:33 starts lecture
class AppUser(AbstractBaseUser, PermissionsMixin):
    personal_number = models.PositiveIntegerField(
        unique=True,
        validators=(validate_len_personal_number,),
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
        max_length=35,
    )
    last_name = models.CharField(
        max_length=35,
    )
    school_grade = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    profile_picture = models.ImageField(
        upload_to='profile-pictures',
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
