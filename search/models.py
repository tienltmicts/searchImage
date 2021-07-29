from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    id_selfie = models.ImageField(upload_to="media/query",default = 'media/query/1.jpg')

    class Meta:
        db_table = "image"
        verbose_name = 'Image'
        verbose_name_plural = 'Image'