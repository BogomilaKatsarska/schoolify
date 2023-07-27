# from django.test import TestCase
# from django.urls import reverse
#
# from schoolify.auth_app.models import Profile
#
#
# class SignUpViewTests(TestCase):
#     VALID_PROFILE_DATA = {
#         'personal_number': '1234567890',
#         'password': '123qwe!@#',
#         'first_name': 'Bogomila',
#         'last_name': 'Katsarska',
#         'school_grade': 9,
#     }
#
#
#     def test_create_profile__when_all_valid__expect_to_create(self):
#         self.client.post(reverse('sign up'), data=self.VALID_PROFILE_DATA)
#
#         profile = Profile.objects.first()
#         # appuser = AppUser.objects.first()
#         self.assertIsNotNone(profile.pk)
#         # self.assertEqual(self.VALID_PROFILE_DATA['personal_number'], appuser.personal_number)
#         # self.assertEqual(self.VALID_PROFILE_DATA['password'], appuser.password)
#         self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
#         self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
#         self.assertEqual(self.VALID_PROFILE_DATA['school_grade'], profile.school_grade)
#
#
#     # def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
#     #     response = self.client.post(
#     #         reverse('create profile'),
#     #         data=self.VALID_PROFILE_DATA,
#     #     )
#     #
#     #     profile = Profile.objects.first()
#     #
#     #     expected_url = reverse('details profile', kwargs={'pk': profile.pk})
#     #     self.assertRedirects(response, expected_url)