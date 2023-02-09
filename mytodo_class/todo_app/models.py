from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='todo_list')
    todo_status = models.BooleanField(
        default=False, blank=True, verbose_name='Completed')
    assign_to = models.ManyToManyField(User, blank=True, related_name='task')
    created_on = models.DateTimeField(
        auto_now=False, auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    archive = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(blank=True)
    commented_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_comments')
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name='todo_comments')
    created_by = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment
