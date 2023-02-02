from django.urls import path
from .views import IndexView, LoginView, LogoutView, TodoDetail, AdminDashboard, AdminCreateTodo
from django.contrib.auth import logout

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='home'),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    path('create-todo/', AdminCreateTodo.as_view(), name='create_todo'),
    path('edit-todo/<int:id>/', TodoDetail.as_view(), name='edit_todo'),
]
