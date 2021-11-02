from django import forms

from courseapp.models import Course, Profession, AdditionalInfo


class CourseEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    target = forms.CharField(widget=forms.Textarea(attrs={'class': 'field textarea', 'cols': '40', 'rows': '5'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label=None, to_field_name="name",
                                        widget=forms.Select(attrs={'class': 'field select select-width'}))

    class Meta:
        model = Course
        fields = ('name', 'location', 'target', 'start_date', 'end_date', 'profession')


class AddCourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=128)
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(),
                                        widget=forms.Select(attrs={'class': 'field select select-width'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=128)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'field', 'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'field', 'type': 'date'}))
    target = forms.CharField(widget=forms.TextInput(attrs={'class': 'field textarea'}), max_length=255)

    class Meta:
        model = Course
        fields = ('name', 'profession', 'location', 'start_date', 'end_date', 'target')


class AddAdditionalInfoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=128)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}), max_length=256, required=False)
    type_info = forms.ChoiceField(choices=AdditionalInfo.TYPE_CHOICES, widget=forms.Select(attrs={
        'class': 'field select select-width'
    }))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'field'}), required=False)
    note = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'field textarea',
        'cols': 40,
        'rows': 5
    }), required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = AdditionalInfo
        fields = ('name', 'description', 'type_info', 'url', 'note', 'file')

class LavelForm(forms.Form):
    
    level = forms.ChoiceField(choices=Course.LEVEL_CHOICES, widget=forms.Select(attrs={
        'class': 'field select'
    }))
  

