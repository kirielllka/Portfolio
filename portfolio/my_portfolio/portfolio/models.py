from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="portfolio/imgs")
    url = models.URLField()