from django.core.exceptions import ValidationError
from django.test import TestCase

from schoolify.auth_app.models import AppUser


class AppUserModelTests(TestCase):
    def test_appuser_save__when_personal_number_is_valid__expect_correct_result(self):
        appuser = AppUser(
            personal_number='1234567890',
            password='123qwe!@#',
            is_staff=False,
        )

        appuser.full_clean()
        appuser.save()

        self.assertIsNotNone(appuser.pk)

    def test_appuser_save__when_personal_number_has_11_digits__expect_exception(self):
        appuser = AppUser(
            personal_number='12345678900',
            password='123qwe!@#',
            is_staff=False,
        )
        with self.assertRaises(ValidationError) as context:
            appuser.full_clean()
            appuser.save()
        self.assertIsNotNone(context.exception)


    def test_appuser_save__when_personal_number_contains_letters_and_digits__expect_exception(self):
        appuser = AppUser(
            personal_number='123456t900',
            password='123qwe!@#',
            is_staff=False,
        )
        with self.assertRaises(ValidationError) as context:
            appuser.full_clean()
            appuser.save()
        self.assertIsNotNone(context.exception)

    def test_appuser_save__when_personal_number_has_contains_space_and_digits__expect_exception(self):
        appuser = AppUser(
            personal_number='123456 900',
            password='123qwe!@#',
            is_staff=False,
        )
        with self.assertRaises(ValidationError) as context:
            appuser.full_clean()
            appuser.save()
        self.assertIsNotNone(context.exception)



