from django.contrib import admin
from django.urls import path, include
from tasks.api import urls as tasks_url
from authentication.api import urls as auth_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(tasks_url)),
    path('api/', include(auth_url))
]
