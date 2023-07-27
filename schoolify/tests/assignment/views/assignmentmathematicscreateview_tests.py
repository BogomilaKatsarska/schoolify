from django.test import TestCase
from django.urls import reverse
from schoolify.assignment.models import AssignmentMathematics


class AssignmentMathematicsCreateViewTest(TestCase):
    VALID_PROFILE_DATA = {
        # 'school_subject': AssignmentMathematics.MUSIC,
        'assignment_name': 'Count to 3',
        'solution': '1,2,3',
    }

    def test_create_assignment_mathematics__when_all_valid__expect_to_create(self):

        self.client.post(
            reverse('assignment mathematics create'),
            data=self.VALID_PROFILE_DATA,
        )

        assignmentmathematics = AssignmentMathematics.objects.get()
        self.assertIsNotNone(assignmentmathematics)
        self.assertEqual(self.VALID_PROFILE_DATA['assignment_name'], assignmentmathematics.assignment_name)
        self.assertEqual(self.VALID_PROFILE_DATA['solution'], assignmentmathematics.solution)

    # def test_create_profile__when_all_valid__expect_to_redirect(self):
    #     response = self.client.post(
    #         reverse('create profile'),
    #         data=self.VALID_PROFILE_DATA,
    #     )
    #
    #     profile = Profile.objects.get()
    #
    #     expected_url = reverse('details profile', kwargs={'pk': profile.pk})
    #     self.assertRedirects(response, expected_url)
