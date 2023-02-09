from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required()
def tasklist(request):
    search = request.GET.get('search')
    if search:

        tasks =Task.objects.filter(title__icontains=search, user=request.user)

    else:
        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user)
        paginator = Paginator(tasks_list, 3)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)
        
    return render(request, 'tasks/list.html', {'tasks': tasks})


def helloworld(request):
    return HttpResponse('ola')

@login_required()
def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required()
def edittask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required()
def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

@login_required()
def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required()
def deletetask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect('/', {'m': 'Tarefa deletada com sucesso!'})
