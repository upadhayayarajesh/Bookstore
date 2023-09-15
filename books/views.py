from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.


class BookListView(ListView):
    model = Book
    templates = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    # to make the default name(object_list) more descriptive
    context_object_name = "book"
    templates = "books/book_detail.html"
