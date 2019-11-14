from django.db import models
from django.utils import timezone

class Camp(models.Model):
    """
    A model for a volunteer work camp
    """
    # Camp information
    title = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    organisation = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    # # Camp Details
    positions = models.IntegerField(null=True)
    positions_female = models.IntegerField(null=True)
    positions_male = models.IntegerField(null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    extra_host_country_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    extra_host_country_fee_currency = models.CharField(default="", max_length=200)

    # # Camp Organising Data
    archived = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length=30, blank=True)

    # Return title str
    def __str__(self):
        return self.title

    # Return title unicode
    def __unicode__(self):
        return self.title

