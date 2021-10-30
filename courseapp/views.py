from django.db.models import Prefetch
import math
from datetime import date
from django.db.models import Q
from django.db.models import Count
from django.views.generic import CreateView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from courseapp.models import Course, AdditionalInfo
from task_app.models import Task, File
from django.urls import reverse_lazy, reverse
from courseapp.forms import CourseEditForm, AddCourseForm, AddAdditionalInfoForm, LavelForm

from django.http import request
from django.shortcuts import get_object_or_404, redirect, HttpResponseRedirect 

from django.shortcuts import render, redirect, HttpResponse

class CourseList(ListView):
    model = Course
    template_name = 'courseapp/courses.html'

    def get_queryset(self):
        return Course.objects.filter(person=self.request.user, is_active=True)

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courseapp/course.html'

    def get_object(self, queryset=None): 
        comment=Count('comments', distinct=True, filter=Q(comments__is_active=True))
        tasks = Prefetch('tasks', Task.objects.filter(is_active=True).annotate(file_task = Count('files', distinct=True), cnt=comment)) 
        addinfo = Prefetch('addinfo', AdditionalInfo.objects.filter(is_active=True).order_by('-create_at'))
        course = Course.objects.prefetch_related(tasks, addinfo).get(id=self.kwargs['pk'])
        for task in course.tasks.all():
            task.check_status()
        return course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs) 
        context['today'] = date.today()
        context['count_task_work'] = Task.objects.filter(Q(status = 'WORK') | Q(status = 'PLAN') | Q(status = 'OVERDUE'), is_active=True, course=(self.get_object()).pk).count()
        context['rate'] = round_rate(self.object.rate)
        context['form'] = LavelForm(initial={'post': self.object}) 
        return context 


class EditCourseView(SuccessMessageMixin, UpdateView):
    form_class = CourseEditForm
    template_name = 'courseapp/edit-course.html'
    model = Course
    extra_context = {'title': 'SkillDiary - Редактирование курса'}
    success_message = 'Все изменения сохранены!'

    def get_success_url(self):
        return reverse_lazy('course:course_edit', args=(self.object.id,))


def update_course_active(request, pk):
    Course.objects.filter(pk=pk).update(is_active='False')
    return redirect('course:course_list')


def update_additional_active(request, pk_course, pk):
    course = get_object_or_404(Course, pk=pk_course)
    AdditionalInfo.objects.filter(pk=pk).update(is_active='False')
    return redirect('course:course_detail', course.pk)

def report_course(request, pk):
    if request.method == 'GET':
        add_report = request.GET.get('add_report')
        Course.objects.filter(pk=pk).update(add_report = add_report)
        return HttpResponse("Success!") 
    else:
        return HttpResponse("Request method is not a GET")

def complete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = LavelForm(request.POST)

    if form.is_valid():
        answer = form.cleaned_data['level']
        Course.objects.filter(pk=pk).update(level=answer)

        task_count = Task.objects.filter(is_active='True', status ='OVERDUE', course = course.pk).count()
       
        if task_count == 0:
            Course.objects.filter(pk=pk).update(status='COMPLETED')
        else:
            Course.objects.filter(pk=pk).update(status='OVERDUE')
    return HttpResponseRedirect(reverse_lazy('course:course_detail', args=(pk,)))


def update_course_status(request, pk):
    
    course = get_object_or_404(Course, pk=pk)
    today = date.today()

    if (today <= course.end_date and today >= course.start_date):
        Course.objects.filter(pk=pk).update(status='WORK')
    else:
        Course.objects.filter(pk=pk).update(status='PLAN')
        
    return redirect('course:course_detail', course.pk)

def round_rate(rate):
    if rate < 10:
        return 0 
    else: 
        return (int(math.floor(rate / 10)) *10)



def course_add(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.person = request.user
            course.save()
            # return redirect('course_list')
    else:
        form = AddCourseForm()
    return render(request, 'courseapp/course-add.html', {'form': form})


class AddAdditionalInfoCreateView(CreateView):
    model = AdditionalInfo
    template_name = 'courseapp/additional-add.html'
    form_class = AddAdditionalInfoForm
    success_url = reverse_lazy('course:course_list')

    def get_context_data(self, **kwargs):
        context = super(AddAdditionalInfoCreateView, self).get_context_data(**kwargs)
        course = get_object_or_404(Course, id=self.kwargs['pk'])

        context.update({
            'course': course,
            'title': 'SkillDiary - Добавление материалов'
        })

        return context

    def form_valid(self, form):
        course = get_object_or_404(Course, id=self.kwargs['pk'])
        form.instance.course = course
        form_valid = super(AddAdditionalInfoCreateView, self).form_valid(form)
        files = form.files.getlist('file')
        for file in files:
            File.objects.create(name=file.name,
                            description=form.cleaned_data['name'],
                            file=file,
                            additional_info=self.object)
        return form_valid

 