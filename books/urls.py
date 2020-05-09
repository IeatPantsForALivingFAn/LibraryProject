from django.urls import path
from . import views
#Url patterns
app_name = 'books'

urlpatterns= [
    path('create/',views.BookCreate.as_view(),name='create'),
    path('<int:pk>/detail/',views.BookDetail.as_view(),name ='detail'),
    path('list/',views.BookList.as_view(),name='list')
]
