from django.contrib.auth.models import User
from django.db import models
# Create your models here.




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    content = models.TextField()
    def __str__(self) -> str:
        return self.tile