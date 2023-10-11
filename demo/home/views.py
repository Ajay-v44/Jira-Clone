from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/login")
def home(request):
    email = request.user.email
    if request.method == "POST":
        data = request.POST
        task = data.get('task')
        Tasks.objects.create(
            task_description=task,
            username=email,
        )
        print(task)
    queryset = Tasks.objects.filter(username=email)

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
        return JsonResponse({'success': True})
    except Tasks.DoesNotExist:
        return JsonResponse({'success': False, 'error_message': 'Task not found'})


def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Use authenticate to verify the user's credentials
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('/login/')

    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)

        if user.exists():

            messages.error(request, 'User Name Already Taken')
        else:

            user = User.objects.create(
                username=email,
                first_name=first_name,
                last_name=last_name,
                email=email,


            )
            user.set_password(password)
            user.save()
            messages.info(request, ' Account Created Successfully ')

            return redirect('/register/')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def delete_page(request):
    queryset = Tasks.objects.all()

    context = {'Tasks': queryset}
    return render(request, 'delete.html',context)
