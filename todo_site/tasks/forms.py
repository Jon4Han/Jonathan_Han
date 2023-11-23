# tasks/test_form.py

from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
   
    class Meta:
        model = Task
        fields = '__all__'


        #fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        # }
        
        
