from django import forms 

from .models import Book


class BookCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": "Title",
            }
        ),
    )
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": "Author",
            }
        ),
    )
    price = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": "Price",
            }
        ),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class BookEditForm(BookCreateForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    price = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
