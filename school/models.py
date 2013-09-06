from django.db import models

class State(models.Model):
    name        = models.CharField(max_length=100, null=False, blank=False)
    code        = models.CharField(max_length=2, null=False, blank=False)
    active      = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class School(models.Model):
    name        = models.CharField(max_length=100, null=False, blank=False)
    address     = models.CharField(max_length=100, null=True, blank=True)
    address2    = models.CharField(max_length=100, null=True, blank=True)
    county      = models.CharField(max_length=100, null=True, blank=True)
    city        = models.CharField(max_length=100, null=True, blank=True)
    state       = models.ForeignKey(State, null=True, blank=True)
    zipcode     = models.CharField(max_length=20, null=True, blank=True)
    phone       = models.CharField(max_length=30, null=True, blank=True)
    fax         = models.CharField(max_length=30, null=True, blank=True)
    website     = models.URLField(null=True, blank=True)
    principal   = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name


