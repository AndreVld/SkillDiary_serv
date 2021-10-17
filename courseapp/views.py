from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView

from mainapp.models import Course


class CourseList(ListView):
    model = Course

    def get_queryset(self):
        return Course.objects.filter(person=self.request.person, is_active=True)


class CourseRead(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseRead, self).get_context_data(**kwargs)
        context["title"] = "курс/просмотр"
        return context
