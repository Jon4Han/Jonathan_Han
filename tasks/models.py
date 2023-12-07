from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=20, null=False,unique=True,error_messages={
        'unique': ("Contact with this Name already exists."),
    })
    email = models.EmailField(blank=False,unique=True)
    notes = models.TextField(max_length=100, default="")
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name