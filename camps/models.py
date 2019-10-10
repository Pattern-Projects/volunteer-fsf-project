from django.db import models
from django.utils import timezone

class Camp(models.Model):
    """
    A model for a volunteer work camp
    """
    title = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=200, blank=False)
    organisation = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    positions = models.IntegerField()
    positions_male = models.IntegerField()
    positions_female = models.IntegerField()
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    extra_host_country_fee = models.DecimalField(max_digits=20, decimal_places=2)
    extra_host_country_fee_currency = models.CharField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)
    published_data = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.title