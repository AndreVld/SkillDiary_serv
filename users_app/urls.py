from django.contrib.auth.views import LogoutView
from django.urls import path, re_path, include
from users_app.views import register, LoginUserView, EditProfileUserView, ProfileView,verify

app_name = 'users_app'

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('registration/', register, name='registration'),
    path('edit_profile/<int:pk>/', EditProfileUserView.as_view(), name='edit_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', verify, name='verify'),


]

