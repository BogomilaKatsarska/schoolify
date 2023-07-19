from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, personal_number, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not personal_number:
            raise ValueError('Personal number must be set')
        user = self.model(personal_number=personal_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, personal_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(personal_number, password, **extra_fields)

    def create_superuser(self, personal_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(personal_number, password, **extra_fields)