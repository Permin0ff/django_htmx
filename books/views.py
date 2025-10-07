from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Book
from .forms import BookCreateForm, BookEditForm


@require_http_methods(['GET'])
def book_list(request):
    book_list = Book.objects.all()
    form = BookCreateForm(auto_id=False)
    return render(
        request,
        'base.html',
        {'book_list': book_list, 'form': form}
    )


@require_http_methods(['POST'])
def create_book(request):
    form = BookCreateForm(request.POST)
    if form.is_valid():
        book = form.save()
    return render(
        request,
        'partial_book_detail.html',
        {'book': book}
    )


def update_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return render(
                request,
                'partial_book_detail.html',
                {'book': book}
            )
    else:
        form = BookEditForm(instance=book)
    return render(
        request,
        'partial_book_update_form.html',
        {'book': book, 'form': form}
    )


@require_http_methods(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(
        request,
        'partial_book_detail.html',
        {'book': book}
    )


@require_http_methods(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse()


@require_http_methods(['PATCH'])
def update_book_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.read = not book.read
    book.save()
    return render(
        request,
        'partial_book_detail.html',
        {'book': book}
    )


@require_http_methods(['GET'])
def book_list_sort(request, filter, direction):
    if direction == 'descend':
        filter = '-' + filter
    book_list = Book.objects.order_by(filter)
    return render(
        request,
        'partial_book_list.html',
        {'book_list': book_list}
    )
