from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()

    return render(request,'task/index.html',{'tasks':tasks})

def detail(request,pk):
    task = Task.objects.get(pk=pk)

    return render(request,'task/detail.html',{'task':task})
# Create your views here.
