from django import forms
from django.conf import settings
from .models import Camp, FilterModel

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('title', 'tagline', 'region', 'country', 'continent', 'organisation', 'description', 'image', 'positions', 'positions_male', 'positions_female', 'positions_other', 
        'required_language', 'start_date', 'end_date', 'price', 'extra_host_country_fee', 'extra_host_country_fee_currency', 'created_date', 'published_date')

    # Add css on init
    def __init__(self, *args, **kwargs):
        super(CampForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'datepicker'        
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'

class CampFilterForm(forms.Form):
    start_after = forms.CharField(required=False)
    end_before = forms.CharField(required=False)

class FilterForm(forms.ModelForm):
    class Meta:
        model = FilterModel
        fields = ('start_after', 'end_before')

    # Add css on init
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['start_after'].widget.attrs['class'] = 'datepicker'        
        self.fields['end_before'].widget.attrs['class'] = 'datepicker'
