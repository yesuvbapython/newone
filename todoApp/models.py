from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoModel(models.Model):
    task = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    