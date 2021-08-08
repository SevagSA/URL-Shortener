from django.db import models

from .utils import create_shortcode


class ShortURL(models.Model):
    url = models.URLField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)
