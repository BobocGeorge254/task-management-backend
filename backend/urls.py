from django.contrib import admin
from django.urls import path, include
from tasks.api import urls as tasks_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(tasks_url))
]
