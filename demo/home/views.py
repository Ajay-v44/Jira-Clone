from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def home(request):
    if request.method =="POST":
        data=request.POST
        task=data.get('task')
        Tasks.objects.create(
            task_description=task,
        )
        print(task)
    queryset=Tasks.objects.all()
   
    context={'Tasks':queryset}

    return render(request,'index.html',context)