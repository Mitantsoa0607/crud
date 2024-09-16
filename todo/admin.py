from django.contrib import admin

from todo.models import Todo, TodoList

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=('id','title','due_date','completed','favourite','todo_list')
    list_filter=('title','due_date','completed')
    search_fields=('title',)

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)