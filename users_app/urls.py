from django.contrib.auth.views import LogoutView
from django.urls import path
from users_app.views import RegistrationView, LoginUserView, EditProfileUserView

app_name = 'users_app'

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('edit_profile/<int:pk>/', EditProfileUserView.as_view(), name='edit_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
