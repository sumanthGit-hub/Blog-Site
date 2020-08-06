from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import StudentForm
from .models import Student

# Create your views here.
@login_required
def upload(request):
    context={}
    if request.method=='POST':
        uploaded_files=request.FILES['document']
        storage=FileSystemStorage()
        name=storage.save(uploaded_files.name,uploaded_files)
        context['url']=storage.url(name)
    return render(request,'Students/upload.html',context)
@login_required
def student_list(request):
    students=Student.objects.all()
    return render(request,'Students/student_list.html',{'students':students})

@login_required
def upload_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Students:student_list')
    else:
        form=StudentForm()
    return render(request,'Students/upload_files.html',{'form':form})

@login_required
def delete_student(request,pk):
    if request.method=='POST':
        students=Student.objects.get(pk=pk)
        students.delete()
    return redirect('Students:student_list')