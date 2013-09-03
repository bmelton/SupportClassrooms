from django.db import models

class Resource(models.Model):
    title       = models.CharField(max_length=255)
    url         = models.URLField(max_length=255)
    source      = models.CharField(max_length=100, null=True, blank=True)
    source_url  = models.URLField(max_length=255, null=True, blank=True)
    date        = models.CharField(max_length=30, null=True, blank=True)
    excerpt     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title
