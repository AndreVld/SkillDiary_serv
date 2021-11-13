from django.conf.urls import url
from django.urls import include, path, re_path
from rest_framework import routers

from api_app import views
from api_app.views import CourseList, UserProfessionList, ProfessionTaskList

router = routers.DefaultRouter()
#router.register(r'persons', views.PersonViewSet)
router.register(r'courses', views.CourseWithOutTaskViewSet, "cwt")
router.register(r'courses_and_task', views.CourseViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'professions', views.ProfessionViewSet)
router.register(r'profile', views.PersonDetailsView,"profile")


urlpatterns = [
    path('', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path('^users/(?P<username>.+)/$', CourseList.as_view()),
    re_path('^user/professions/$', UserProfessionList.as_view()),
    re_path('^user/professions_and_task/$', ProfessionTaskList),


]