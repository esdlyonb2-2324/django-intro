from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'

class Message(models.Model):

    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default="missing_author")

