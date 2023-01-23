from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from .models import Todo


class IndexView(View):
    """
    homepage for the app
    """

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        todos = user.task.all()
        complete_task = user.task.filter(todo_status=True).count()
        progress_task = user.task.filter(todo_status=False).count()
        return render(request, 'index.html', {'todos': todos, 'completed_count': complete_task, 'inprogress_count': progress_task})


class TodoDetail(View):
    """
    edit and get the todo detail
    """

    def get(self, request, id):
        todo = Todo.objects.filter(id=id)
        return render(request, 'edit-todo.html', {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.filter(pk=id)
        if request.method == "POST":
            todo_status = request.POST.get('status', False)
            if todo_status == 'on':
                todo_status = True
            todo.update(todo_status=todo_status)
            return render(request, 'edit-todo.html', {'todo': todo, 'message': 'Todo Updated'})
        else:
            return render(request, 'edit-todo.html', {'todo': todo, 'message': 'Something went wrong'})


class LoginView(View):
    """
    Login for the users
    """

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            msg = "User/Password does not match"
            return render(request, 'login.html', {'message': msg})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
