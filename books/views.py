from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book


# Create your views here.


class BookListView(ListView):
    model = Book
    templates = "books/book_list.html"
