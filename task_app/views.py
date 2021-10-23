from django.db.models import Prefetch
from django.urls import reverse_lazy, resolve
from django.views.generic import DetailView, CreateView, UpdateView

from courseapp.models import Course
from task_app.forms import TaskAddForm, CommentAddForm, FileAddForm
from task_app.models import Task, Comment


class TaskView(DetailView):
    template_name = 'task_app/task.html'
    extra_context = {'title': 'SkillDiary -'}
    context_object_name = 'task'

    def get_object(self, queryset=None):
        comments = Prefetch('comments', Comment.objects.order_by('-create_at'))
        task_id = self.kwargs.get('task_id')
        return Task.objects.prefetch_related(comments, 'files').get(id=task_id)


class TaskAddView(CreateView):
    form_class = TaskAddForm
    template_name = 'task_app/task-add.html'
    extra_context = {'title': 'SkillDiary -'}

    def form_valid(self, form):
        form.instance.course = Course.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        return super(TaskAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskAddView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        return context

    def get_success_url(self):
        return reverse_lazy('tasks:task', kwargs={'pk': self.kwargs['pk'], 'task_id': self.object.pk})


class TaskEditView(UpdateView):
    form_class = TaskAddForm
    template_name = 'task_app/task-edit.html'
    extra_context = {'title': 'SkillDiary -'}

    def get_object(self, queryset=None):
        return Task.objects.get(id=self.kwargs['task_id'])

    def get_context_data(self, **kwargs):
        context = super(TaskEditView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        return context

    def get_success_url(self):
        return reverse_lazy('tasks:task', kwargs=self.kwargs, )


class CommentAddView(CreateView):
    form_class = CommentAddForm
    template_name = 'task_app/comment-add.html'
    extra_context = {'title': 'SkillDiary -'}

    def get_context_data(self, **kwargs):
        context = super(CommentAddView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        context['task'] = Task.objects.values('name').get(id=self.kwargs.get('task_id'))
        return context

    def form_valid(self, form):
        form.instance.task = Task.objects.get(pk=self.kwargs['task_id'])
        return super(CommentAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks:task', kwargs=self.kwargs, )


class FileAddView(CreateView):
    form_class = FileAddForm
    template_name = 'task_app/file-add.html'
    extra_context = {'title': 'SkillDiary -'}

    def get_context_data(self, **kwargs):
        context = super(FileAddView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        context['task'] = Task.objects.values('name').get(id=self.kwargs.get('task_id'))
        return context

    def form_valid(self, form):
        form.instance.task = Task.objects.get(pk=self.kwargs['task_id'])
        return super(FileAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks:task', kwargs=self.kwargs)
