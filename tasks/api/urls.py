from django.urls import path
from .views import TaskListApiView, TaskDetailApiView, TaskUserApiView

urlpatterns = [
    path('tasks/', TaskListApiView.as_view(), name='task-list'),
    path('tasks/<int:task_id>/', TaskDetailApiView.as_view(), name='task-detail'),
    path('users/tasks/<int:user_id>/', TaskUserApiView.as_view(), name='task-user'),
]
