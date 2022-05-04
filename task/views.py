from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from .models import Task, User
from django.contrib.auth.decorators import login_required
from .forms import TaskFormView, TaskUpdateForm
# Create your views here.

@login_required
def task(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        "tasks": tasks
    }
    return render(request,'task/task_list.html', context)

@login_required
def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task": task
    }
    return render(request,'task/task_detail.html', context)

@login_required
def task_add_view(request):
    if request.POST:
        form = TaskFormView(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
    else:
        form = TaskFormView()

    context = {
        "form": form
    }
    return render(request,'task/task_add.html', context)


@login_required
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.POST:
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskUpdateForm(instance=task)
            
    context = {
        "form": form
    }
    return render(request,'task/task_update.html', context)

@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    
    return redirect('task:task-list')
