from django.urls import re_path
import courseapp.views as courseapp
from courseapp.apps import CourseappConfig

app_name = CourseappConfig.name

urlpatterns = [
    re_path(r"^$", courseapp.CourseList.as_view(), name="courses_list"),
    re_path(r"^read/(?P<pk>\d+)/$", courseapp.CourseRead.as_view(), name="course_read"),
]