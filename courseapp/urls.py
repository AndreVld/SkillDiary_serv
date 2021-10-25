from django.urls import re_path
from django.urls import path
import courseapp.views as courseapp
from courseapp.apps import CourseappConfig

app_name = CourseappConfig.name

urlpatterns = [
    path("courses/", courseapp.CourseList.as_view(), name='course_list'),
    path("courses/add/", courseapp.course_add, name='course_add'),
    #re_path(r"^$", courseapp.CourseList.as_view(), name="courses_list"),
    #re_path(r"^read/(?P<pk>\d+)/$", courseapp.CourseRead.as_view(), name="course_read"),
]