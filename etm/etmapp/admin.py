from django.contrib import admin

from .models import Role, UserData, Project, Task

# Register your models here.



admin.site.register(Role)
admin.site.register(UserData)
admin.site.register(Project)
admin.site.register(Task)
