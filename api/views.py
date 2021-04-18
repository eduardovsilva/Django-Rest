from rest_framework import viewsets
from .serializers import TaskSerializer
from tarefas_app.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
