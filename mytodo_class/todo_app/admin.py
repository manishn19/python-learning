from django.contrib import admin
from .models import Todo, Comment


class AdminTodo(admin.ModelAdmin):
    """
    Todo filter by column for admin section
    """
    list_filter = ('todo_status', 'created_on', 'assign_to')


admin.site.register(Todo, AdminTodo)


class AdminComment(admin.ModelAdmin):
    """
    Comment filter and display columns for admin section
    """
    list_display = ('comment', 'commented_by', 'created_by')
    list_filter = ('created_by', 'commented_by')


admin.site.register(Comment, AdminComment)
