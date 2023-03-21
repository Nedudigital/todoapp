from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .form import TaskForm
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect) 
from .models import Task
# Create your views here.

#class TaskList(ListView):
    #model = Task 
    #context_object_name = 'tasks'

def list_view(request):
    context = {}
    context["dataset"] = Task.objects.all()

    return render(request, "task_list.html", context)


#class TaskDetail(DetailView):
    model = Task   
    context_object_name = 'task'
#def detail_view(request, id):
    context ={}
    context["data"] = Tasks.object.get(id = id)
    return render(request, "todolist/task.detail.html", context)

#def update_view(request, id):
    context ={}
    obj = get_object_or_404(Task, id = id)

    form = TaskForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    
    context["form"] = form

    return render(request, "todolist/task_update.html", context)

#class TaskCreate(CreateView):
    model = Task
    field = '__all__'
    success_url = reverse_lazy('tasks')

def update_view(request, id):
    id = int(id)
    try:
        task_todo = Task.objects.get(id = id)
    except Task.DoesNotExist:
        return redirect('index')
    form = TaskForm(request.POST or None, instance = task_todo)
    if form.is_valid():
       form.save()
       return redirect('index')
    return render(request, 'todolist/task_form.html', {'task_form':form})

def create_view(request):
    context = {}

    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "todolist/task_create.html", context) 


def delete_view(request, id):
    id = int(id)
    try:
        task_todo = Task.objects.get(id = id)
    except Task.DoesNotExist:
        return redirect('index')
    task_todo.delete()
    return redirect('index')

