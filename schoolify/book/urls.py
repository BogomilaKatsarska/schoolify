from django.urls import path

from schoolify.book.views import BooksListView, book_a_book_functionality

urlpatterns = (
    path('list/', BooksListView.as_view(), name='books list'),
    path('book-enquiry/<int:book_id>', book_a_book_functionality, name="book enquiry"),
)