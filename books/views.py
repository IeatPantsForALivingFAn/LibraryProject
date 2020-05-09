from django.shortcuts import render
from django.urls import reverse
from django.views.generic import edit
from django.views import generic
from .forms import BookForm
from .models import Book
from django.http import HttpResponse
from django.contrib.auth import mixins
# Create your views here.
class BookCreate(edit.CreateView,mixins.LoginRequiredMixin):
    model = Book
    fields = ['name','author','available','copies']
    template_name = 'books/book_create.html'

class BookDetail(generic.DetailView,mixins.LoginRequiredMixin):
    model = Book
    template_name = 'books/book_view.html'
class BookList(generic.ListView,mixins.LoginRequiredMixin):
    model = Book
    paginate_by = 50
