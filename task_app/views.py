from django.views.generic import DetailView

from task_app.models import Task


class TaskView(DetailView):
    template_name = 'task_app/task.html'
    extra_context = {'title': 'SkillDiary -'}
    context_object_name = 'task'

    def get_queryset(self):
        task_id = self.kwargs.get('pk')
        return Task.objects.prefetch_related('comments', 'files').filter(pk=task_id)
