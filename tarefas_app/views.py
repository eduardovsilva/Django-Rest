from django.shortcuts import render, redirect, reverse, get_object_or_404
from tarefas_app.forms import TaskForm
from tarefas_app.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tarefas_app/list-task.html', {'tasks': tasks})


def add_tasks(request):
    form = TaskForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:tasks'))
    return render(request, 'tarefas_app/form-task.html', {'form': form})


def remove_tasks(request, task_pk):
    task = get_object_or_404(Task.objects, pk=task_pk)

    task.delete()

    return redirect(reverse('tasks:tasks'))


def complete_tasks(request, task_pk):
    task = get_object_or_404(Task.objects, pk=task_pk)

    task.is_completed = 'completed'
    task.save()

    return redirect(reverse('tasks:tasks'))
