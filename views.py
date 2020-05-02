from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def dashboard(request):
    return render(request,'dashboard.html')

def register(request):
    return render(request,'register.html')
