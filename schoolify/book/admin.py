from django.contrib import admin

from schoolify.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ['name', 'author']
    search_fields = ('name',)

