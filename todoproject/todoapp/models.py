from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
class c_Todo(models.Model):
    complete = models.BooleanField(default=False)
    title=Todo.title
    description=Todo.description
    prirority=Todo.priority
    created_at=Todo.created_at