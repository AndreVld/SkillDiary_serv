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
    path('course_complete/<int:pk>/', courseapp.complete_course, name='course_complete'),
    path('course_report/<int:pk>/', courseapp.report_course, name='course_report'),
    path('additional_delete/<int:pk_course>/<int:pk>/', courseapp.update_additional_active, name='additional_delete'),

    path("courses/add/", courseapp.course_add, name='course_add'),

    path('add-additional/<int:pk>/', courseapp.AddAdditionalInfoCreateView.as_view(), name='additional_add'),
]