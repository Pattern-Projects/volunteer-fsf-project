from django import forms
from .models import Camp

class UserLoginForm(forms.Form):
    """Form for user login"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Create forms
class CampForm(forms.ModelForm):
    """Form for creating and editing camp"""
    class Meta:
        model = Camp
        fields = ('name', 'available')

