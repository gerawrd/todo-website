from django import forms
from .models import Task

class TaskFormView(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'complete', 'user')
        exclude = ('user',)