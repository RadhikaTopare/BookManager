# books/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publish_date','rating', 'status', 'poster']
        widgets = {
                'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }
