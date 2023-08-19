from django.shortcuts import render, redirect
from task_management.forms import TaskForm
from task_management.models import TaskModel
# Create your views here.


def manage_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print(task.cleaned_data)
            return redirect ('ShowTask')
    
    else:
        task = TaskForm()
    return render(request, 'home.html', {'form' :task})

def show_tasks(request):
    task = TaskModel.objects.all()
    print(task)
    return render(request, 'show_task.html', {'data': task})
def complete(request):
    task = TaskModel.objects.all()
    print(task)
    return render(request, 'completed_task.html', {'data': task})

def edit_tasks(request, id):
    task = TaskModel.objects.get(pk = id)
    form = TaskForm(instance= task)
    if request.method == 'POST':
        info = TaskForm(request.POST, instance= task)
        if info.is_valid():
            info.save()
            return redirect ('ShowTask')
    return render(request, 'home.html', {'form' :form})

def delete_tasks(request, id):
    task = TaskModel.objects.get(pk = id).delete()
    return redirect('ShowTask')

def completed_tasks(request, id):
    task = TaskModel.objects.get(pk = id)
    task.is_completed = True
    task.save()
    return redirect ('Completed')

