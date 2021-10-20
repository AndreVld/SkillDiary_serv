from django.urls import path

from task_app.views import TaskView, TaskAddView

app_name = 'task_app'

urlpatterns = [
    path('task/<int:pk>/', TaskView.as_view(), name='task'),
    path('add_task/', TaskAddView.as_view(), name='add_task'),
]