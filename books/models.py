import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)

    class Meta:
        """This method is to set the permission to the user"""
        permissions = [
            ("special_status", "Call read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class Review(models.Model):
    # for many to one field we must also specify an on_delete option.
    # we also explicitly set the related_name to make it easier to follow the foreign key relation
    # backwards in the future projects.
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review
