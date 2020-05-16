from django import forms
from .models import Book
#forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=['name','author','available','copies']
class BookSearch(forms.Form):
    book_info = forms.CharField()
    
