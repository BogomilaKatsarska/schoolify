import datetime
from django.test import TestCase
from schoolify.book.models import Book


class BookModelTests(TestCase):

    def test_book_save__when_everything_is_valid__expect_correct_result(self):
        book = Book(
            name='Mathematics Book',
            author='Anyone',
            description='This is the book description',
            school_subject=Book.TYPES_OF_SUBJECTS[0][0],
            number_of_pages=300,
            available_from=datetime.datetime.today(),
        )

        book.full_clean()
        book.save()

        self.assertIsNotNone(book.pk)
        self.assertEqual(book.name, 'Mathematics Book')
        self.assertEqual(book.author, 'Anyone')
        self.assertEqual(book.description, 'This is the book description')
        self.assertEqual(book.school_subject, 'Mathematics')
        self.assertEqual(book.number_of_pages, 300)
        self.assertEqual(book.available_from, datetime.date.today())
        self.assertIsNone(book.cover_image)
