from django.urls import path
from .views import IndexView, LoginView, LogoutView, TodoDetail
from django.contrib.auth import logout

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='home'),
    path('edit-todo/<int:id>/', TodoDetail.as_view(), name='edit_todo'),
]
