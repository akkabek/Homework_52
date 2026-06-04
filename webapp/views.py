from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, STATUS_CHOICES


def task_list(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        ids = request.POST.getlist('task_ids')
        if ids:
            Task.objects.filter(pk__in=ids).delete()
        return redirect('task_list')
    return render(request, 'webapp/task_list.html', {'tasks': tasks})


def task_add(request):
    if request.method == 'POST':
        description = request.POST.get('description', '').strip()
        details = request.POST.get('details', '').strip()
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date') or None
        if description:
            Task.objects.create(
                description=description,
                details=details,
                status=status,
                due_date=due_date
            )
        return redirect('task_list')
    return render(request, 'webapp/task_add.html',
                  {'status_choices': STATUS_CHOICES,
                  'task' : Task()
                   })

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'webapp/task_confirm_delete.html', {'task': task})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'webapp/task_detail.html', {'task': task})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'webapp/task_update.html', {
            'task': task,
            'status_choices': STATUS_CHOICES,
        })
    elif request.method == 'POST':
        task.description = request.POST.get('description', '').strip()
        task.details = request.POST.get('details', '').strip()
        task.status = request.POST.get('status', 'new')
        task.due_date = request.POST.get('due_date') or None
        task.save()
        return redirect('task_detail', pk)
