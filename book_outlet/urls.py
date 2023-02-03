from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:id>", views.book_detail, name="book-detail-page"),
]
