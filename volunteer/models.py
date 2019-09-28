from django.db import models

# Create your models here.
class Camp(models.Model):
    name = models.CharField(max_length=30, blank=False)
    available = models.BooleanField(blank=False, default=True)
    
    def __str__(self):
        return self.name