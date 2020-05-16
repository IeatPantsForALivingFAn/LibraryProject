from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import edit
from django.views import generic
from .forms import BookForm, BookSearch
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

def search_book(request):
    if request.method == 'POST':
        book = Book.objects.filter(name__icontains=request.POST['search'])
        book_author = Book.objects.filter(author__icontains=request.POST['search'])
        return render(request,'books/book_list.html',context={
                                            'book_by_name':book,
                                            'book_by_author':book_author,
                                            })
