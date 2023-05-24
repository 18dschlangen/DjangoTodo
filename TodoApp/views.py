from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoItemForm
from django.utils import timezone


def todo_list(request):
    form = TodoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TodoItemForm()  # Clear the form after saving

    todos = TodoItem.objects.all()
    context = {'todos': todos, 'form': form}
    return render(request, 'todo_list.html', context)

def delete_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

def complete_todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    todo.completed = True
    todo.completed_date = timezone.now()  # set completed_date to current time
    todo.save()
    return redirect('todo_list')

def edit_todo(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    form = TodoItemForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'edit_todo.html', {'form': form})


