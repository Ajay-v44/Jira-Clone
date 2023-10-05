from django.shortcuts import render
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

    return render(request,'index.html')