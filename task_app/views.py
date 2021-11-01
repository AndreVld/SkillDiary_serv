from datetime import date

from django.db.models import Count
from django.db.models import Q
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, resolve
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.shortcuts import get_object_or_404

from courseapp.models import Course
from task_app.forms import TaskAddForm, CommentAddForm, FileAddForm
from task_app.models import Task, Comment


class TaskView(DetailView):
    template_name = 'task_app/task.html'
    extra_context = {'title': 'SkillDiary -'}
    context_object_name = 'task'

    def get_object(self, queryset=None):
        comments = Prefetch('comments', Comment.objects.filter(is_active=True).order_by('-create_at'))
        task_id = self.kwargs.get('task_id')
        return Task.objects.prefetch_related(comments, 'files').get(id=task_id, is_active=True)


class TaskAddView(CreateView):
    form_class = TaskAddForm
    template_name = 'task_app/task-add.html'
    extra_context = {'title': 'SkillDiary -'}

    def form_valid(self, form):
        form.instance.course = Course.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        if form.cleaned_data['start_date'] > date.today():
            form.instance.status = 'PLAN'
        return super(TaskAddView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TaskAddView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        context['course'] = Course.objects.values('name').get(id=self.kwargs.get('pk'))
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
        context['course'] = Course.objects.values('name').get(id=self.kwargs.get('pk'))
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
        context['course'] = Course.objects.values('name').get(id=self.kwargs.get('pk'))
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
        context['course'] = Course.objects.values('name').get(id=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.task = Task.objects.get(pk=self.kwargs['task_id'])
        return super(FileAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tasks:task', kwargs=self.kwargs)


def delete_task(request, pk, task_id):
    Task.objects.filter(id=task_id).update(is_active='False')
    return HttpResponseRedirect(reverse_lazy('course:course_detail', args=(pk,)))


def complete_task(request, pk, task_id):
    Task.objects.filter(id=task_id).update(status='COMPLETED')
    return HttpResponseRedirect(reverse_lazy('course:course_detail', args=(pk,)))


class TaskList(ListView):
    template_name = 'task_app/task-daily.html'

    def get_queryset(self):
        comment=Count('comments', distinct=True, filter=Q(comments__is_active=True))
        return Task.objects.filter(user=self.request.user, is_active=True, end_date=date.today(), status = 'WORK').annotate(file_task = Count('files', distinct=True), cnt=comment)

def delete_comment(request, pk, task_id, comment_id):
    task = get_object_or_404(Task, pk=task_id)
    Comment.objects.filter(pk=comment_id).update(is_active='False')
    return HttpResponseRedirect(reverse_lazy('tasks:task', args=(pk,task.pk, )))

    
