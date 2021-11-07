from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views.generic.base import TemplateView
from users_app.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users_app.models import Person
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import auth, messages
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from courseapp.models import Course
from django.http import request


def send_verify_mail(user):
    verify_link = reverse('users_app:verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = Person.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key = ''
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'users_app/verification.html')
        else:
            del user
            print(f'error activation user 1')
            return render(request, 'users_app/verification.html')
    except Exception as e:
        print(f'error activation user 2: {e.args}')
        return HttpResponseRedirect(reverse('users_app:login'))


class LoginUserView(LoginView):
    template_name = 'users_app/login.html'
    form_class = UserLoginForm
    extra_context = {'title': 'SkillDiary - Авторизация'}


def register(request):
    title = 'SkillDiary - Регистрация'

    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                messages.success(request, 'Verify code sending')
                return HttpResponseRedirect(reverse('users_app:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('users_app:login'))
    else:
        register_form = UserRegistrationForm()

    content = {'title': title, 'form': register_form}
    return render(request, 'users_app/registration.html', content)


# class RegistrationView(CreateView):
#     # model = Person
#     # form_class = UserRegistrationForm
#     # template_name = 'users_app/registration.html'
#     # extra_context = {'title': 'SkillDiary - Регистрация'}
#     # success_url = reverse_lazy('users:login')
#
#


class ProfileView(TemplateView):
    model = Person
    template_name = 'users_app/profile.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SkillDiary - Профиль'
        context['media_url'] = settings.MEDIA_URL
        rate_sum = 0
        courses = Course.objects.filter(is_active=True, person=self.request.user)
        for course in courses:
            rate_sum += course.rate  
        rate = int(rate_sum / len(courses))
        self.request.user.rate = rate
   
        return context
   
 

class EditProfileUserView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users_app/edit_profile.html'
    model = Person
    extra_context = {'title': 'SkillDiary - Редактирование прфиля'}
    success_message = 'Все изменения сохранены!'

    def get_success_url(self):
        return reverse_lazy('users:edit_profile', args=(self.object.id,))

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')
