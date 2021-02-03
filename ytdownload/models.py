from django.db import models

# Create your models here.
class videos(models.Model):
    video = models.FileField(upload_to='videos')