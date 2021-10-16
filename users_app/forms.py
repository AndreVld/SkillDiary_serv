from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users_app.models import Person, City


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'field',
              }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'field',
              }
    ))

    class Meta:
        model = Person
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'field',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'field',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'field'}))

    class Meta:
        model = Person
        fields = ('username', 'email', 'password1',)


class UserProfileForm(UserChangeForm):
    #username = forms.CharField(widget=forms.TextInput(attrs={'class': ''}),required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), required=False)
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'id':'input_avatar', 'class':'avatar-edit'}), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'field'}), required=False)
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.Select(attrs={'class': 'field select select-width'}), required=False)

    class Meta:
        model = Person
        fields = ( 'first_name', 'last_name', 'surname', 'age', 'city', 'avatar', 'email')
