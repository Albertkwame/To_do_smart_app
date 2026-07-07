from django.shortcuts import render
from .models import TodoItem
from .form import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all().order_by('-created_at')
    form = TodoItemForm()
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'todos': todos})


def todo_detail(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'update.html', {'form': form, 'todo': todo})

def todo_delete(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'delete.html', {'todo': todo})