from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.






class Role(models.Model):
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.role

class UserData(models.Model):
    username = models.ForeignKey(User,on_delete=models.DO_NOTHING,unique=True)
    email = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField(max_length=10,unique=True)
    birthday = models.DateField()
    role = models.ForeignKey(Role,on_delete=models.DO_NOTHING)
    assigned_project = models.CharField(max_length=50,default='')
    join_date = models.DateField()
    image = models.ImageField(upload_to='images',unique=True)

    def __str__(self):
        return self.first_name + '---' + self.last_name  + '---' + self.assigned_project



class Project(models.Model):
    client = models.CharField(max_length=30)
    project_name = models.CharField(max_length=30)
    project_detail = models.TextField(default='')
    # manager = UserData.objects.filter(role='admin')
    docx = models.TextField(default='')
    team = models.TextField(default='')
    start_date = models.DateField(default=datetime.date.today())
    deadline = models.DateField(default=datetime.date.today())
    comments = models.TextField(default='')

    def __str__(self):
        return self.project_name


class Task(models.Model):
    title = models.CharField(max_length=30)
    task_of = models.ForeignKey(Project,on_delete=models.DO_NOTHING)
    details = models.TextField()
    assign_to = models.ForeignKey(UserData,on_delete=models.DO_NOTHING)
    docx = models.TextField()
    task_start = models.DateField(default=datetime.date.today())
    task_deadline = models.DateField(default=datetime.date.today())



