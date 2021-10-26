from django import forms

from task_app.models import Task, Comment, File


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'start_date', 'end_date',)

    def __init__(self, *args, **kwargs):
        super(TaskAddForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'field'


class CommentAddForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'field textarea'}))

    class Meta:
        model = Comment
        fields = ('text',)


class FileAddForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'field textarea'}), required=False)
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'title-field'}))

    class Meta:
        model = File
        fields = ('name', 'description', 'file',)
