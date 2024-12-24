# registration/forms.py
from django import forms
from .models import Player  # Ensure you have a Player model defined

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['username', 'email', 'studio_associato']  # Adjust fields as necessary