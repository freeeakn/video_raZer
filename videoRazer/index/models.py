from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=200, null=False)
    category = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=255, null=False)
