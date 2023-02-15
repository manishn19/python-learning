from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, get_object_or_404
from .models import Todo
from .forms import CommentForm, AddTodoForm


class IndexView(View):
    """
    homepage for the app
    """

    # def test_func(self):
    #     """
    #     validate the user only
    #     """
    #     return not self.request.user.is_superuser

    def get(self, request):
        # redirect on login page
        if not request.user.is_authenticated:
            return redirect('login')

        # Redirect the super user to dashboard
        if self.request.user.is_superuser:
            return redirect('dashboard')

        user = User.objects.get(id=request.user.id)
        todos = user.task.all()
        complete_task = user.task.filter(todo_status=True).count()
        progress_task = user.task.filter(todo_status=False).count()
        archive_task = user.task.filter(archive=True).count()

        return render(request, 'index.html', {'todos': todos, 'completed_count': complete_task, 'inprogress_count': progress_task, 'archive_count': archive_task})


class TodoDetail(View):
    """
    edit and get the todo detail
    """

    def update_todo_users(self, existing_user, new_user, todo):
        list_user = []
        for uid in existing_user:
            list_user.append(uid.id)

        if new_user == list_user:
            return False
        else:
            todo = todo.first()
            # remove all the previous users from current todo
            for user_id in existing_user:
                todo.assign_to.remove(user_id)

            # assign new users to current todo
            for user_id in new_user:
                todo.assign_to.add(user_id)

            return True

    def get(self, request, id):
        todo = Todo.objects.filter(id=id)
        users = User.objects.filter(is_superuser=False)
        form = CommentForm()
        return render(request, 'edit-todo.html', {'todo': todo, 'form': form, 'users': users})

    def post(self, request, id):
        todo = Todo.objects.filter(pk=id)
        existing_user = todo.first().assign_to.all()
        assigned_user = []
        form = CommentForm()
        if 'todo-form' in request.POST:
            todo_status = request.POST.get('status', False)
            if todo_status == 'on':
                todo_status = True
            # save data from Admin only
            if self.request.user.is_superuser:
                todo.title = request.POST.get('title')
                todo.description = request.POST.get('description')
                # get all selected user
                assigned = request.POST.getlist('assign_to')
                for userid in assigned:
                    assigned_user.append(int(userid))

                # call the function for updating/removing users from this todo
                user_updates = self.update_todo_users(
                    existing_user, assigned_user, todo)
                todo.update(title=todo.title, description=todo.description)

            todo.update(todo_status=todo_status)
            messages.success(
                request, (f'Todo Updated'))
            return redirect(f'/edit-todo/{id}/')
            # return redirect('home')
        elif 'post-comment' in request.POST:
            form = CommentForm(request.POST)
            current_todo = Todo.objects.filter(pk=id).first()
            current_user = User.objects.filter(id=request.user.id).first()
            if form.is_valid():
                comment = form.save(commit=False)
                comment.todo = current_todo
                comment.commented_by = current_user
                comment.save()
            return redirect(f'/edit-todo/{id}/')
        else:
            return render(request, 'edit-todo.html', {'todo': todo, 'message': 'Something went wrong'})


class AdminDashboard(UserPassesTestMixin, View):
    """
    only admin can use this dashboard
    """
    login_url = '/login/'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        todos = Todo.objects.all()
        complete_task = todos.filter(todo_status=True).count()
        progress_task = todos.filter(todo_status=False).count()
        archive_task = todos.filter(archive=True).count()
        return render(request, 'dashboard.html', {'todos': todos, 'completed': complete_task, 'progress': progress_task, 'archive_count': archive_task})


class AdminCreateTodo(UserPassesTestMixin, View):
    """
    Only admin can create new Todo
    """
    login_url = '/login/'
    # template_name = 'create-todo.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        form = AddTodoForm()
        return render(request, 'create-todo.html', {'form': form})

    def post(self, request):
        form = AddTodoForm(request.POST)
        if form.is_valid:
            todo = form.save(commit=False)
            todo.created_by = self.request.user
            todo.save()
            form.save_m2m()
            return render(request, 'create-todo.html', {'form': form, 'message': 'A Todo added!'})


def todo_archive(request, id):
    todo = Todo.objects.get(id=id)
    if todo.archive == True:
        todo.archive = False
    else:
        todo.archive = True
    todo.save()
    return redirect('dashboard')


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('dashboard')


class TodoArchive(UserPassesTestMixin, View):
    """
    Archive the todo
    """

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return redirect(request, 'archive-todo.html', {'todo': todo})

    def post(self, request, id):
        todo = Todo.objects.get(pk=id)
        todo.archive = True
        todo.save()
        return redirect(request, 'dashboard.html')


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
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect(reverse('home'))
        else:
            msg = "User/Password does not match"
            return render(request, 'login.html', {'message': msg})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
