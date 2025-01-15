from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#model for user
class User):
    first = models.CharField(max_length=50,null=False)
    last = models.CharField(max_length=50,null=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
        
MODEL_CHOICES = (
    ('pending', 'Pending'),
    ('inprogress', 'In Progress'),
    ('completed', 'Completed'),
    ('overdue', 'Overdue'),
)
#model for task
class Task(models.Model):
    title = models.CharField(max_length=225, null=False)
    description = models.TextField(null=False)
    due_date = models.DateField(null=False)
    priority = models.IntegerField(null=False)
    status = models.CharField(max_length=50, choices=MODEL_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

#model for comment
class Comment(models.Model):
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
        
