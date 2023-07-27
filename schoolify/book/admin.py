from django.contrib import admin

from schoolify.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

