import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from schoolify.book.forms import BookCreateForm
from schoolify.book.models import Book


class BookCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'book.add_book'
    template_name = 'book/books-create.html'
    form_class = BookCreateForm
    success_url = reverse_lazy('books list')


class BooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/books-list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('name')
        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(name__icontains=pattern.lower())

        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


@login_required
def book_a_book_functionality(request, book_id):
    book = Book.objects.get(pk=book_id)
    if book.available_from > date.today():
        book.available_from += datetime.timedelta(days=5)
        book.last_booked_by = request.user

    else:
        book.available_from = date.today() + datetime.timedelta(days=5)
    book.save()

    return redirect('books list')
