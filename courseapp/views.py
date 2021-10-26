from datetime import date
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin
from courseapp.models import Course, AdditionalInfo
from task_app.models import Task, File
from django.urls import reverse_lazy
from courseapp.forms import CourseEditForm, AddCourseForm, AddAdditionalInfoForm

from django.http import request
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render, redirect

class CourseList(ListView):
    model = Course
    template_name = 'courseapp/courses.html'

    def get_queryset(self):
        return Course.objects.filter(person=self.request.user, is_active=True)


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courseapp/course.html'

    def get_context_data(self, **kwargs):
        tasks = Task.objects.filter(is_active=True, course=(self.get_object()).pk)
        for task in tasks:
            task.check_status()

        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["title"] = "курс/просмотр"
        context["additionals"] = AdditionalInfo.objects.filter(is_active=True, course=(self.get_object()).pk)
        context["tasks"] = tasks
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


def update_course_status(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if (course.status == 'COMPLETED'):
        today = date.today()
        if (today > course.end_date):
            Course.objects.filter(pk=pk).update(status='OVERDUE')
        elif (today <= course.end_date and today >= course.start_date):
            Course.objects.filter(pk=pk).update(status='WORK')
        else:
            Course.objects.filter(pk=pk).update(status='PLAN')
    else:
        Course.objects.filter(pk=pk).update(status='COMPLETED')
    return redirect('course:course_detail', course.pk)


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
        File.objects.create(name=form.cleaned_data['name'],
                            description=form.cleaned_data['name'],
                            file=form.cleaned_data['file'],
                            additional_info=self.object)
        return form_valid
