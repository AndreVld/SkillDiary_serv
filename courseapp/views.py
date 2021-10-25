from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView
from courseapp.models import Course
from courseapp.forms import AddCourseForm
from django.shortcuts import render, redirect


class CourseList(ListView):
    model = Course
    template_name = 'courseapp/courses.html'
    def get_queryset(self):
        return Course.objects.filter(person=self.request.user, is_active=True)

"""
class CourseRead(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseRead, self).get_context_data(**kwargs)
        context["title"] = "курс/просмотр"
        return context
"""


def course_add(request):
    if request.method == "POST":
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.person = request.user
            course.save()
            #return redirect('course_list')
    else:
        form = AddCourseForm()
    return render(request, 'courseapp/course-add.html', {'form': form})

"""
class AddCourseView(CreateView):
    form_class = AddCourseForm
    template_name = 'courseapp/course-add.html'
    extra_context = {'title': 'SkillDiary -'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCourseView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddCourseView, self).get_context_data()
        context['current_url'] = resolve(self.request.path_info)
        return context

    def get_success_url(self):
        return reverse('tasks:task', kwargs=self.kwargs,)
"""