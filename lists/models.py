from django.db import models
from school.models import School

class Category(models.Model):
    school      = models.ForeignKey(School)
    name        = models.CharField(max_length=80)
    list_count  = models.PositiveIntegerField(default=0)
    active      = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s" % (self.school.name, self.name)

    class Meta:
        verbose_name_plural = "categories"

class List(models.Model):
    school      = models.ForeignKey(School)
    category    = models.ForeignKey(Category, null=True, blank=True)
    name        = models.CharField(max_length=80)
    active      = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s %s" % (self.school.name, self.name)

class Item(models.Model):
    school      = models.ForeignKey(School)
    category    = models.ForeignKey(Category, null=True, blank=True)
    list        = models.ForeignKey(List)
    active      = models.BooleanField(default=True)

    name        = models.CharField(max_length=80)
    url         = models.URLField()
    image       = models.URLField(null=True, blank=True)
    price       = models.CharField(max_length=20, null=True, blank=True)
    asin        = models.CharField(max_length=20, null=True, blank=True)
    quantity    = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return "%s" % (self.name)

class Type(models.Model):
    name        = models.CharField(max_length=80)
    active      = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

class MasterItem(models.Model):
    type        = models.ForeignKey(Type)
    active      = models.BooleanField(default=True)

    name        = models.CharField(max_length=80)
    url         = models.URLField()
    image       = models.URLField(null=True, blank=True)
    price       = models.CharField(max_length=20, null=True, blank=True)
    asin        = models.CharField(max_length=20, null=True, blank=True)
    quantity    = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return "%s" % (self.name)
