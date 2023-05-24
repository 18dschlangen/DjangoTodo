from .views import todo_list, delete_todo, complete_todo, edit_todo
from django.urls import path

urlpatterns = [
    path('todos/', todo_list, name='todo_list'),
    path('todos/delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('todos/complete/<int:todo_id>/', complete_todo, name='complete_todo'),
    path('todos/edit/<int:todo_id>/', edit_todo, name='edit_todo'),
]
