from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def complete(self):
        self.completed = True
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title