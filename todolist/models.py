from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    is_finished = models.BooleanField(default=False)