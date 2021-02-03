from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='useruploads')

class Video(models.Model):
    video = models.FileField(upload_to='videos', default='')