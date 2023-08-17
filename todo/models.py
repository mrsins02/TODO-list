from django.db import models
from django.contrib.auth.models import User


class TodoDetail(models.Model):
    description = models.TextField(blank=True, null=True)
    reminder_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "TODO Detail"
        verbose_name_plural = "TODO Details"


class Todo(models.Model):
    todo_message = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    details = models.OneToOneField(TodoDetail, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.todo_message}({self.user})"

    class Meta:
        verbose_name = "TODO"
        verbose_name_plural = "TODOs"
