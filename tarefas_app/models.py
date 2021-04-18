from django.db import models

# Create your models here.


class Task(models.Model):
    TASK_STATUS = [
        ('completed', 'Completed'),
        ('uncompleted', 'Uncompleted')
    ]

    name = models.CharField(max_length=20)
    description = models.TextField()
    is_completed = models.CharField(
        "Status", default='uncompleted', choices=TASK_STATUS, max_length=15)
