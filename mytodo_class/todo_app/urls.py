from django.urls import path
from .views import *
from django.contrib.auth import logout

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    path('create-todo/', AdminCreateTodo.as_view(), name='create_todo'),
    path('edit-todo/<int:id>/', TodoDetail.as_view(), name='edit_todo'),
    # path('archive/<int:id>/', TodoArchive.as_view(), name='archive'),
    path('archive/<int:id>/', todo_archive, name='archive'),
    path('delete/<int:id>/', todo_delete, name='delete'),
]
