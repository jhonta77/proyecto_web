from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm

def task_list_and_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    tasks = task.objects.all()
    return render(request, 'task_list.html', {'form': form, 'tasks': tasks})
