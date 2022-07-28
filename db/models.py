from django.db import models

from django.contrib.auth import models as auth_models

# Create your models here.
class Task(models.Model):
    descr = models.CharField(max_length=200)
    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE, null=True)