from django.shortcuts import render, redirect
from .forms import *
from .models import TodoModel


def index(request):
    model = TodoModel.objects.all()
    form = TodoModelForm()
    count_task = model.count()
    completed_task = TodoModel.objects.filter(complete=True)
    count_completed_task = completed_task.count()
    count_uncompleted_task = count_task - count_completed_task

    if 'q' in request.GET:
        q = request.GET['q']
        model = TodoModel.objects.filter(task__icontains=q)
    else:
        model = TodoModel.objects.all()

    if request.method == 'POST':
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = TodoModelForm()
    context = {'models': model, 'form': form, 'total': count_task, 'completed': count_completed_task, 'uncompleted': count_uncompleted_task,}
    return render(request, 'main/index.html', context)


def delete(request, id):
    model = TodoModel(id=id)
    if request.method == 'POST':
        model.delete()
        return redirect('/')
    return render(request, 'main/delete.html', {})


def update(request, id):
    model = TodoModel.objects.get(id=id)
    form = UpdateTodoForm(request.POST or None, instance=model)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'main/update.html', context)
