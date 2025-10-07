from django.urls import path

from .views import (
    book_list,
    create_book,
    update_book_details,
    book_detail,
    delete_book,
    update_book_status,
    book_list_sort,
)


urlpatterns = [
    path(
        '',
        book_list,
        name='book_list'
    ),
    path(
        'create_book/',
        create_book,
        name='create_book'
    ),
    path(
        'update_book_details/<int:pk>/',
        update_book_details,
        name='update_book_details'
    ),
    path(
        'book_detail/<int:pk>/',
        book_detail,
        name='book_detail'
    ),
    path(
        'delete_book/<int:pk>/',
        delete_book,
        name='delete_book'
    ),
    path(
        'update_book_status/<int:pk>/',
        update_book_status,
        name='update_book_status'
    ),
    path(
        'book_list_sort/<filter>/<direction>/',
        book_list_sort,
        name='book_list_sort'
    ),
]
