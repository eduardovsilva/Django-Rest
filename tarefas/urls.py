from django.contrib import admin
from django.urls import path, include
from tarefas_app import urls as tasks_urls
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include((tasks_urls, 'list'), namespace='tasks')),
    path('api/', include(api_urls, namespace='api')),
]
