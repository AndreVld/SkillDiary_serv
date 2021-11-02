from django.urls import path
from django.views.generic.edit import DeleteView

from task_app.views import   CommentEditView, FileDelete, TaskView, TaskAddView, CommentAddView, TaskEditView, FileAddView, delete_task, complete_task, delete_comment

app_name = 'task_app'

urlpatterns = [
    path('task/<int:task_id>/', TaskView.as_view(), name='task'),
    path('add_task/', TaskAddView.as_view(), name='add_task'),
    path('task/<int:task_id>/edit_task/', TaskEditView.as_view(), name='edit_task'),
    path('task/<int:task_id>/add_comment/', CommentAddView.as_view(), name='add_comment'),
    path('task/<int:task_id>/add_file/', FileAddView.as_view(), name='add_file'),
    path('task/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('task/<int:task_id>/complete_task/', complete_task, name='complete_task'),
    path('task/<int:task_id>/delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('task/<int:task_id>/edit_comment/<int:comment_id>/', CommentEditView.as_view(), name='edit_comment'),
    path('task/<int:task_id>/delete_file/<int:file_id>/', FileDelete.as_view(), name='delete_file'),
]
