from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from api_app import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'professions', views.ProfessionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))


]