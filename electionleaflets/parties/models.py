from django.db import models
from core.models import Country
from core.util import AutoSlugField


class Party(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey( Country )
    logo_file = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)
    colour = models.CharField(max_length=18, blank=True)
    twitter_account = models.CharField(max_length=150, blank=True)
    slug = AutoSlugField(max_length=100, populate_from='name')
    
    def __unicode__(self):
        return self.name