"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('completed_tasks/<int:id>/', completed_tasks, name='completed_tasks'),
    path('deleted_tasks/<int:id>/', deleted_tasks, name='deleted_tasks'),
    path('remove_tasks/<int:id>/', remove_tasks, name='remove_tasks'),
    # Add the URL pattern for updating the task status
    path('update_task_status/<int:id>/<str:status>/', update_task_status, name='update_task_status'),
]
