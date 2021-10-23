from django.urls import path

from task_app.views import TaskView, TaskAddView, CommentAddView, TaskEditView, FileAddView

app_name = 'task_app'

urlpatterns = [
    path('task/<int:task_id>/', TaskView.as_view(), name='task'),
    path('add_task/', TaskAddView.as_view(), name='add_task'),
    path('task/<int:task_id>/edit_task/', TaskEditView.as_view(), name='edit_task'),
    path('task/<int:task_id>/add_comment/', CommentAddView.as_view(), name='add_comment'),
    path('task/<int:task_id>/add_file/', FileAddView.as_view(), name='add_file'),
]
