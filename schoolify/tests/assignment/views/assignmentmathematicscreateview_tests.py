from django.test import TestCase
from django.urls import reverse

from schoolify.assignment.models import AssignmentMathematics

#TODO: CHECK THIS TEST !!!!!!!!!
class AssignmentMathematicsCreateViewTest(TestCase):
    VALID_MATHEMATICS_ASSIGNMENT_DATA = {
        # 'school_subject': AssignmentMathematics.MATHEMATICS,
        'assignment_name': 'Count to 3',
        'solution': '1, 2, 3',
    }

    def test_create_assignment_mathematics__when_all_valid__expect_to_create(self):
        self.client.post(reverse('assignment mathematics create'), data=self.VALID_MATHEMATICS_ASSIGNMENT_DATA)

        assignment_mathematics = AssignmentMathematics.objects.get()
        self.assertIsNotNone(assignment_mathematics)
        self.assertEqual(self.VALID_MATHEMATICS_ASSIGNMENT_DATA['assignment_name'], assignment_mathematics.assignment_name)
        self.assertEqual(self.VALID_MATHEMATICS_ASSIGNMENT_DATA['solution'], assignment_mathematics.solution)
