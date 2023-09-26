from django.db import models

# Create your models here.
class shlModel(models.Model):
    title = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    frontend = models.CharField(max_length=255)
    backend = models.CharField(max_length=255)
    databases = models.CharField(max_length=255)
    infrastructure = models.CharField(max_length=255)