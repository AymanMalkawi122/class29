from django.db import models
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    assignee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('task_list')