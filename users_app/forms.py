from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users_app.models import Person, City


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'style': 'border: 1px solid #66C1DE; box-sizing: border-box;border-radius: 26px;',
               'placeholder': 'Введите имя пользователя'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'style': 'border: 1px solid #66C1DE; box-sizing: border-box;border-radius: 26px;',
               'placeholder': 'Введите пароль'}
    ))

    class Meta:
        model = Person
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. почты'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = Person
        fields = ('username', 'email', 'password',)


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': '', 'readonly': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': ''}), required=False)
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': ''}), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': ''}), required=False)
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.Select(attrs={'class': ''}), required=False)

    class Meta:
        model = Person
        fields = ('username', 'first_name', 'last_name', 'surname', 'age', 'city', 'avatar', 'email')
