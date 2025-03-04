from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.core.signals import request_started
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import StudentForm, RegisterForm
from .models import Students
#crud - create,read,update,delete

# Create your views here.



@login_required
def student_list(request):
    student=Students.objects.all()
    return render(request, 'studentlist.html',{'student':student})
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
            form=StudentForm()
            return render(request,'student_form.html',{'form':form})
def delete_student(request, id):
   student=Students.objects.get(id=id)
   student.delete()
   return redirect('student_list')
def update_student(request, id):
    student=Students.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
    else:
        form=StudentForm(instance=student)
        return render(request,'student_form.html',{'form':form})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('student_list')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('student_list')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html',{'form':form})
def logout_user(request):
    logout(request)
    return redirect('login')
