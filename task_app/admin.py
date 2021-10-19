from django.contrib import admin

# Register your models here.
from task_app.models import Task, Comment, File

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(File)
