from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Students
#crud - create,read,update,delete

# Create your views here.
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

