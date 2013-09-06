from django.db import models

class Quote(models.Model):
    quote       = models.TextField()
    attribution = models.CharField(max_length=100)
    active      = models.BooleanField(default=True)

    def __unicode__(self):
        return "'%s' - %s" % (self.quote, self.attribution)
        return self.quote

    def get(self):
        return Quote.objects.order_by('?')[0]
