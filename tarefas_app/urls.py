from django.urls import path
from .views import index, add_tasks, remove_tasks, complete_tasks


app_name = "tarefas_app"

urlpatterns = [
    path('', index, name='tasks'),
    path('add/', add_tasks, name='add'),
    path('<int:task_pk>/remove/', remove_tasks, name='remove'),
    path('<int:task_pk>/complete/', complete_tasks, name='complete'),
]
