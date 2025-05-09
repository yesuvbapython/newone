from django import forms
from .models import todoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = todoModel
        fields = ['task']