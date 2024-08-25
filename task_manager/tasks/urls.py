from . import views
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    else:
        return redirect('login')

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('completed/', views.completed_tasks, name='completed_tasks'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.task_create, name='task_create'),
    path('task/edit/<int:task_id>/', views.task_edit, name='task_edit'),

]
