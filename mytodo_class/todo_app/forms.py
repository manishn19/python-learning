from .models import Comment, Todo
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'assign_to']
