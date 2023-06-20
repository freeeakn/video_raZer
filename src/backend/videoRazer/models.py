from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()
    

class Video(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=200, null=False)
    category = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=255, null=False)