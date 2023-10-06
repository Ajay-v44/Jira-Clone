from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse


# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        task = data.get('task')
        Tasks.objects.create(
            task_description=task,
        )
        print(task)
    queryset = Tasks.objects.all()

    context = {'Tasks': queryset}

    return render(request, 'index.html', context)


def completed_tasks(request, id):
    queryset = Tasks.objects.get(id=id)
    queryset.status = "completed"
    queryset.save()
    return redirect('home')


def deleted_tasks(request, id):
    try:
        queryset = Tasks.objects.get(id=id)
        queryset.status = "deleted"

        queryset.save()
       
        return redirect('home')
    except Tasks.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Task not found'})


def remove_tasks(request, id):
    queryset = Tasks.objects.get(id=id)
    queryset.status = "removed"
    queryset.save()
    return redirect('home')
def update_task_status(request, id, status):
    try:
        task = Tasks.objects.get(id=id)
        task.status = status
        task.save()
        return redirect('home')
    except Tasks.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Task not found'})