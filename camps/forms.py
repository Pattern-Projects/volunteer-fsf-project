from django import forms
from .models import Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('title', 'region', 'country', 'continent', 'organisation', 'description', 'image', 'positions', 'positions_male', 'positions_female', 'positions_other', 
        'required_language', 'start_date', 'end_date', 'extra_host_country_fee', 'extra_host_country_fee_currency', 'created_date', 'published_date', 'tag')
