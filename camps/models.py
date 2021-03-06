from django.db import models
from django.utils import timezone
from datetime import date

class Camp(models.Model):
    """
    A model for a volunteer work camp
    """

    # Camp information
    title = models.CharField(max_length=200, blank=False)
    tagline = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    CONTINENTS = [('ASIA','Asia'),('AFRICA','Africa'),('AUSTRALIA', 'Australia'),('AMERICAS', 'Americas'),('EUROPE', 'Europe'),]
    continent = models.CharField(max_length=10, choices=CONTINENTS, default=1)
    organisation = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    # Camp Details
    positions = models.PositiveIntegerField(default=0, null=True)
    positions_female = models.PositiveIntegerField(default=0, null=True)
    positions_male = models.PositiveIntegerField(default=0, null=True)
    positions_other = models.PositiveIntegerField(default=0, null=True)
    required_language = models.CharField(max_length=200, blank=True, default="English")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    extra_host_country_fee = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True)
    extra_host_country_fee_currency = models.CharField(default="", max_length=200, blank=True)

    # Camp Organising Data
    archived = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    # Return title str
    def __str__(self):
        return self.title

    # Return title unicode
    def __unicode__(self):
        return self.title

class FilterModel(models.Model):
    start_after = models.DateField(default=date.today)
    end_before = models.DateField(default=date.today)
    