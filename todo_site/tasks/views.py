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
#from .forms import ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_url')  # Redirect to a new URL
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})

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