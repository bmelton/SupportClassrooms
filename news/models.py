from django.db import models

from datetime import datetime

class News(models.Model):
    title       = models.CharField(max_length=255)
    body        = models.TextField(null=True, blank=True)
    date        = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        verbose_name        = "News"
