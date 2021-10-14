from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users_app.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users_app.models import Person


class LoginUserView(LoginView):
    template_name = 'users_app/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'SkillDiary - Авторизация'}


class RegistrationView(CreateView):
    model = Person
    form_class = UserRegistrationForm
    template_name = 'users_app/registration.html'
    extra_context = {'title': 'SkillDiary - Регистрация'}
    success_url = reverse_lazy('users:login')


class EditProfileUserView(SuccessMessageMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users_app/edit_profile.html'
    model = Person
    extra_context = {'title': 'SkillDiary - Редактирование прфиля'}
    success_message = 'Все изменения сохранены!'

    def get_success_url(self):
        return reverse_lazy('users:edit_profile', args=(self.object.id,))
