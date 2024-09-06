from django.forms import ModelForm, CharField, TextInput
from .models import Book


class BookCreateForm(ModelForm):
    title = CharField(required=False, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Title"}))
    author = CharField(required=False, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Author"}))
    price = CharField(required=False, widget=TextInput(attrs={"class": "clrtxt", "placeholder": "Price"}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class BookEditForm(BookCreateForm):
    title  = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
    author = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
    price  = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
