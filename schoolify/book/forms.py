from django import forms

from schoolify.book.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['last_booked_by'].widget.attrs['readonly'] = True
        self.fields['last_booked_by'].widget.attrs['disabled'] = True
        self.fields['name'].widget.attrs['placeholder'] = 'Please fill in the name of the book'
        self.fields['author'].widget.attrs['placeholder'] = 'Please fill in the name of the author'
        self.fields['description'].widget.attrs['placeholder'] = 'Please fill in description(if any)'
        self.fields['number_of_pages'].widget.attrs['placeholder'] = 'Please fill in number of pages(if known)'
        self.fields['available_from'].widget.attrs['placeholder'] = 'Please fill in the appropriate date'
        self.fields['cover_image'].widget.attrs['placeholder'] = 'Please upload cover image(if available)'
