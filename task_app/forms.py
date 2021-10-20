from django import forms

from courseapp.models import Course
from task_app.models import Task


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'start_date', 'end_date', )

    def __init__(self, *args, **kwargs):
        super(TaskAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field'
