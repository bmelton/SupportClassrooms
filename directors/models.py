from django.db import models

class Director(models.Model):
    name        = models.CharField(max_length=255)
    title       = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    picture     = models.URLField(null=True, blank=True)
    email       = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name
