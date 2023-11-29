from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from django.shortcuts import render, redirect

class TaskListView(ListView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")

class TaskDetailView(DetailView):
    model = Task
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list")

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")