from django import forms
from .models import Camp

# Create forms
class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('name', 'available')