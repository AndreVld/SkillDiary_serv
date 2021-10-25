from django.urls import re_path
from django.urls import path
import courseapp.views as courseapp
from courseapp.apps import CourseappConfig

app_name = CourseappConfig.name

urlpatterns = [
    path('courses/', courseapp.CourseList.as_view(),  name='course_list'),
    path('course/<int:pk>/', courseapp.CourseDetailView.as_view(), name='course_detail'),
    path('course_edit/<int:pk>/', courseapp.EditCourseView.as_view(), name='course_edit'),
    path('course_delete/<int:pk>/', courseapp.update_course_active, name='course_delete'),
    path('course_update_status/<int:pk>/', courseapp.update_course_status, name='course_update_status'),
    path('additional_delete/<int:pk_course>/<int:pk>', courseapp.update_additional_active, name='additional_delete'),
    # path('search_tasks/<int:pk>/', courseapp.search_tasks, name='search_tasks'),
    #path("add_course/", courseapp.add_course),
    #re_path(r"^$", courseapp.CourseList.as_view(), name="courses_list"),
    #re_path(r"^read/(?P<pk>\d+)/$", courseapp.CourseRead.as_view(), name="course_read"),
]