from django.urls import path
from . import views
#Url patterns
app_name = 'students'

urlpatterns=[
    path('signup/',views.studentsignup, name='signup'),
    path('<int:pk>/detail/',views.StudentDetailView.as_view(),name='detail'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('thnks/',views.Thanks.as_view(), name='thnks'),
]
