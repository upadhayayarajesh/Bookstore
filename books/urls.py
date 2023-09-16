from django.urls import path

from books.views import BookListView, BookDetailView, SearchResultView

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultView.as_view(), name="searchResult"),
]
