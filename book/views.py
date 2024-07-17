from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from .models import book

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class booksListView(ListView):
    model= book
    template_name = "books_list.html"
    context_object_name = "books_objs"

class bookDetailsView(DetailView):
    model = book
    template_name = "book_details.html"
