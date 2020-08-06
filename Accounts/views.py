from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView,TemplateView


# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'About.html')

def SignUp(request):
    if request.method=='POST':
        form=forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=forms.UserCreateForm()
    return render(request,'registration/signup.html',{'form':form})