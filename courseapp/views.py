from datetime import date
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from courseapp.models import Course, AdditionalInfo
from task_app.models import Task
from django.urls import reverse_lazy
from courseapp.forms import CourseEditForm

from django.http import request
from django.shortcuts import get_object_or_404, redirect


class CourseList(ListView):
    model = Course
    template_name = 'courseapp/courses.html'
    def get_queryset(self):
        return Course.objects.filter(person=self.request.user, is_active=True)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courseapp/course.html'

    def get_context_data(self, **kwargs):
        
        tasks =  Task.objects.filter(is_active=True, course = (self.get_object()).pk) 

        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["title"] = "курс/просмотр"
        context ["additionals"] = AdditionalInfo.objects.filter(is_active=True, course = (self.get_object()).pk)
        context ["tasks"] = tasks
        return context

    

class EditCourseView(SuccessMessageMixin,UpdateView):
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
    course = get_object_or_404(Course,pk=pk_course)
    AdditionalInfo.objects.filter(pk=pk).update(is_active='False')
    return redirect('course:course_detail', course.pk)


def update_course_status(request, pk):
    course = get_object_or_404(Course,pk=pk)

    if (course.status == 'COMPLETED'):
        today = date.today()
        if ( today > course.end_date):
            Course.objects.filter(pk=pk).update(status= 'OVERDUE')
        elif ( today <= course.end_date and today >= course.start_date):
            Course.objects.filter(pk=pk).update(status= 'WORK')
        else: 
            Course.objects.filter(pk=pk).update(status= 'PLAN')
    else: 
        Course.objects.filter(pk=pk).update(status= 'COMPLETED' )
    return redirect('course:course_detail', course.pk)



