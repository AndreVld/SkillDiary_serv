from django import forms
from courseapp.models import Course, Profession


class AddCourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=128)
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), widget=forms.Select(attrs={'class': 'field select select-width'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=128)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'field', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'field', 'type': 'date'}))
    target = forms.CharField(widget=forms.TextInput(attrs={'class': 'field textarea'}), max_length=255)

    class Meta:
        model = Course
        fields = ( 'name', 'profession', 'location', 'start_date', 'end_date', 'target')