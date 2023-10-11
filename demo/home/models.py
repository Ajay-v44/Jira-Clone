from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    task_description = models.CharField(max_length=100)
    status = models.CharField(default="pending", max_length=50)
