from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    task = models.CharField(max_length=255)
    estimated_time = models.IntegerField(blank=False)
    elapsed_time = models.IntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.task