from django import forms
from .models import TodoModel


class TodoModelForm(forms.ModelForm):
    task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Add you task...'}))

    class Meta:
        model = TodoModel
        fields = ['task']


class UpdateTodoForm(forms.ModelForm):
    task = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Add you task...'}))

    class Meta:
        model = TodoModel
        fields = ['task', 'complete']