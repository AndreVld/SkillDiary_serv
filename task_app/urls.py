from django.urls import path

from task_app.views import TaskView

app_name = 'task_app'

urlpatterns = [
    path('<int:pk>/', TaskView.as_view(), name='task'),
    # path('<int:pk>/add_task/', TaskAddView.as_view(), name='add_task'),
]