from django.db import models

# Create your models here.


class CaptionImage(models.Model):
    image = models.ImageField(upload_to='img/')


class OCRImage(models.Model):
    image = models.ImageField()
