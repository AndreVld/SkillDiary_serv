from django import forms
from django.core.exceptions import ValidationError
from courseapp.models import Course, Profession, AdditionalInfo
from task_app.models import Task

class CourseEditForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput()) 
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    target = forms.CharField(widget=forms.Textarea(attrs={'class': 'field textarea', 'cols': '40', 'rows': '5'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='name', to_field_name="name",
                                        widget=forms.Select(attrs={'class': 'field select select-width'}))

    class Meta:
        model = Course
        fields = ('id', 'name', 'location', 'target', 'start_date', 'end_date', 'profession')

    def __init__(self, *args, **kwargs):    
        super(CourseEditForm, self).__init__(*args, **kwargs) 
        if self.data.get('id') == None: 
            try: 
                course_id = Course.objects.last().id 
                self.fields['id'].initial = course_id + 1
            except AttributeError: 
                 self.fields['id'].initial = 1
              
    def clean(self):
        
        cleaned_data = self.cleaned_data
        id = cleaned_data.get('id')
        end_date = cleaned_data.get('end_date')
        start_date = cleaned_data.get('start_date')
    
        task = Task.objects.filter(course = id, is_active = True)
        if task:
            start_date_task = (min(task.values_list('start_date')))[0]
            end_date_task = (min(task.values_list('end_date')))[0]
            if start_date >  start_date_task: 
                self.add_error('start_date', ValidationError('У вас есть задачи, сроки, которых начинаются раньше курса '))
        
            if end_date  < end_date_task: 
                self.add_error('end_date', ValidationError('У вас есть задачи, сроки, которых оканчиваются позже курса '))

        if end_date < start_date:          
                 self.add_error('start_date', ValidationError('Дата начала не может быть больше даты окончания'))
        return cleaned_data


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
  

