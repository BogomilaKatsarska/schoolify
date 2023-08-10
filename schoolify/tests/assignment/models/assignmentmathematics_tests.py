from django.core.exceptions import ValidationError
from django.urls import reverse
from django.test import TestCase
from schoolify.assignment.models import AssignmentMathematics
from schoolify.auth_app.models import Profile, AppUser


class AssignmentMathematicsTests(TestCase):
    VALID_PROFILE_DATA = {
        'personal_number': 1234567890,
        'password1': '123qwe!@#',
        'password2': '123qwe!@#',
        'first_name': 'Bogomila',
        'last_name': 'Katsarska',
        'school_grade': 9,
    }

    def test_assignment_mathematics_save__when_everything_is_valid__expect_correct_result(self):

        self.client.post(reverse('sign up'), data=self.VALID_PROFILE_DATA)
        appuser = AppUser.objects.first()

        assignment_mathematics = AssignmentMathematics(
            school_subject=AssignmentMathematics.TYPES_OF_SUBJECTS[0][0],
            assignment_name='This is my first assignment name',
            created_by=appuser,
            solution='12312312312312',
        )

        assignment_mathematics.full_clean()
        assignment_mathematics.save()

        self.assertIsNotNone(assignment_mathematics.pk)
        self.assertEqual(assignment_mathematics.school_subject, 'Mathematics')
        self.assertEqual(assignment_mathematics.assignment_name, 'This is my first assignment name')
        self.assertEqual(assignment_mathematics.created_by, appuser)
        self.assertEqual(assignment_mathematics.solution, '12312312312312')

