from django.urls import path

from schoolify.book.views import BooksListView

urlpatterns = (
    path('list/', BooksListView.as_view(), name='books list'),
)