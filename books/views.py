from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView

from books.models import Book


# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    templates = "books/book_list.html"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    # to make the default name(object_list) more descriptive
    context_object_name = "book"
    templates = "books/book_detail.html"
    permission_required = "books.special_status"


class SearchResultView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
