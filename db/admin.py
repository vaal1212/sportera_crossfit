from django.contrib import admin

from . models import Task

# Register your models here.
# class 

class TaskAdmin(admin.ModelAdmin):
    list_display = ['descr', 'author']

admin.site.register(Task, TaskAdmin)