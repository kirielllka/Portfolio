from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    date = models.DateField(auto_now=False, auto_now_add=False)
