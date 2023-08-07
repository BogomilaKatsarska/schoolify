import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from schoolify.book.models import Book


class BooksListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/books-list.html'
    paginate_by = 3
    total_books = Book.objects.count()
    total_english_books = Book.objects.filter(school_subject='English').count()
    total_mathematics_books = Book.objects.filter(school_subject='Mathematics').count()
    total_music_books = Book.objects.filter(school_subject='Music').count()
    total_cooking_books = Book.objects.filter(school_subject='Cooking').count()
    extra_context = {
        'total_books': total_books,
        'total_english_books': total_english_books,
        'total_mathematics_books': total_mathematics_books,
        'total_music_books': total_music_books,
        'total_cooking_books': total_cooking_books,
    }

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

    else:
        book.available_from = date.today() + datetime.timedelta(days=5)
    book.save()

    return redirect('books list')


class BookCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'book.add_book'
    template_name = 'book/books-create.html'
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books list')
