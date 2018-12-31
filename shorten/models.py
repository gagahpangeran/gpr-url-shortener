from django.db import models

# Create your models here.


class ShortenLink(models.Model):
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()
    slug = models.SlugField()
