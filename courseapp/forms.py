from django import forms


from courseapp.models import Course, Profession

    


class CourseEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    target = forms.CharField(widget=forms.Textarea(attrs={'class': 'field textarea','cols':'40', 'rows':'5'}))
    start_date =  forms.DateField(widget = forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    end_date = forms.DateField(widget = forms.DateInput(attrs={'type': 'date', 'class': 'field'}))
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), empty_label=None, to_field_name="name", widget=forms.Select(attrs={'class': 'field select select-width'}))    
    class Meta:
        model = Course
        fields = ( 'name', 'location', 'target', 'start_date', 'end_date', 'profession')

    