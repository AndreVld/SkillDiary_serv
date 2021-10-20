from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from courseapp.models import Course
from task_app.forms import TaskAddForm
from task_app.models import Task


class TaskView(DetailView):
    template_name = 'task_app/task.html'
    extra_context = {'title': 'SkillDiary -'}
    context_object_name = 'task'

    def get_queryset(self):
        task_id = self.kwargs.get('pk')
        return Task.objects.prefetch_related('comments', 'files').filter(pk=task_id)


class TaskAddView(CreateView):
    form_class = TaskAddForm
    template_name = 'task_app/task-add.html'

    def form_valid(self, form):
        form.instance.course = Course.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super(TaskAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:profile', )
        #     return reverse_lazy('path to course', args=(self.kwargs.get('pk'),))
