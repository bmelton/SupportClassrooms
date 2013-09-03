from django.db import models

STATES = (
    ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"),
    ("CA", "California"), ("CO", "Colorado"), ("CT", "Connecticut"),
    ("DE", "Delaware"), ("FL", "Florida"), ("GA", "Georgia"), ("HI", "Hawaii"),
    ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"), ("IA", "Iowa"),
    ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"),
    ("MD", "Maryland"), ("MA", "Massachussetts"), ("MI", "Michigan"),
    ("MN", "Minnesota"), ("MS", "Mississippi"), ("MO", "Missouri"),
    ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"),
    ("NH", "New Hampshire"), ("NJ", "New Jersey"), ("NM", "New Mexico"),
    ("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"),
    ("OH", "Ohio"), ("OK", "Oklahoma"), ("OR", "Oregon"),
    ("PA", "Pennsylvania"), ("RI", "Rhode Island"), ("SC", "South Carolina"),
    ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"),
    ("UT", "Utah"), ("VT", "Vermont"), ("VA", "Virginia"),
    ("WA", "Washington"), ("WV", "West Virginia"), ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)

class School(models.Model):
    name        = models.CharField(max_length=100, null=False, blank=False)
    address     = models.CharField(max_length=100, null=True, blank=True)
    address2    = models.CharField(max_length=100, null=True, blank=True)
    county      = models.CharField(max_length=100, null=True, blank=True)
    city        = models.CharField(max_length=100, null=True, blank=True)
    state       = models.CharField(max_length=2, choices=STATES, null=True, blank=True)
    zipcode     = models.CharField(max_length=20, null=True, blank=True)
    phone       = models.CharField(max_length=30, null=True, blank=True)
    fax         = models.CharField(max_length=30, null=True, blank=True)
    website     = models.URLField(null=True, blank=True)
    principal   = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.name


