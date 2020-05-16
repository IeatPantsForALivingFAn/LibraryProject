from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views import generic
from .forms import StudentSignUpForm,Login
from .models import Student, User
from django.contrib.auth import mixins, login, logout, authenticate
# Create your views here.
def studentsignup(request):
    if request.method =='POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll_no = form.cleaned_data['roll_no']
            sem = form.cleaned_data['sem']
            branch = form.cleaned_data['branch']
            email = form.cleaned_data['email']
            password = form.cleaned_data['set_password']
            # create user
            user = User(username = name,email= email)
            user.set_password(password)
            user.save()
            # create Student
            student = Student(user=user,name=name,roll_no=roll_no,sem=sem,branch=branch )
            student.save()

            return HttpResponseRedirect(reverse('students:login'))
        else:
            print('form not valid')
            return render(request,'students/signup.html',{'form':form})

    else:
        form = StudentSignUpForm()
        return render(request,'students/signup.html',{'form':form})

def loginPage(request):
    if request.method=='POST':
        #if request method is post
        form = Login(request.POST)
        print('method is post')
        if form.is_valid():
            # if form is valid then
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                # if user exists then
                login(request,user)
                print('student login done')
                return HttpResponseRedirect(reverse('students:detail',args=[user.student.pk]))
                # if user has entered invalid Credentials or not present
            else:
                print('invalid Credentials')
                message = 'Invalid Credentials or SignUp'
                form = Login()
                return render(request,'students/login.html',context={'message':message,'form':form})
        else:
            print('invalid form')
            message = 'Invalid form'
            return render(request,'students/login.html',context={'message':message,'form':form})
    else:
        #if request method is get
        form = Login()
        return render(request, 'students/login.html',{'form':form})

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('students:thnks'))

class Thanks(generic.TemplateView):
    template_name='students/thanks.html'

class StudentDetailView(mixins.LoginRequiredMixin,generic.DetailView):
    model = Student
    template_name = 'students/student_detail.html'
