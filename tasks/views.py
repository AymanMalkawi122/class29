from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Task


class TaskListView(ListView):
    template_name = "tasks/task_list.html"
    model = Task


class TaskDetailView(DetailView):
    template_name = "tasks/task_detail.html"
    model = Task


class TaskCreateView(CreateView):
    template_name = "tasks/task_create.html"
    model = Task
    fields = ['name', 'desc', 'assignee', 'status']


class TaskUpdateView(UpdateView):
    template_name = "tasks/task_update.html"
    model = Task
    fields = ['name', 'desc', 'status']


class TaskDeleteView(DeleteView):
    template_name = "tasks/task_delete.html"
    model = Task
    success_url = reverse_lazy("task_list")