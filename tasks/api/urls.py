from django.urls import path
from .views import TaskListApiView, TaskDetailApiView

urlpatterns = [
    path('tasks/', TaskListApiView.as_view(), name='task-list'),
    path('tasks/<int:task_id>/', TaskDetailApiView.as_view(), name='task-detail'),
]
