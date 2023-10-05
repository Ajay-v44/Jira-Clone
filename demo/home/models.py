from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_description=models.CharField(max_length=100)
    status=models.CharField(default="pending",max_length=50)