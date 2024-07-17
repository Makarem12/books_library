from django.contrib import admin
from django.urls import path
from .views import HomePageView, booksListView, bookDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('booksList', booksListView.as_view(), name='books'),
    path('<int:pk>', bookDetailsView.as_view(), name="book_details")
]