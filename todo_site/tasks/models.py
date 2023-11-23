
# Create your models here.
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=20, null=False,unique=True)
    email = models.EmailField(blank=True)
    notes = models.TextField(max_length=100, default="")
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
