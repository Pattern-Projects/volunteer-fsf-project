from django import forms
from .models import Camp

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('title', 'country', 'organisation', 'description', 'image')

