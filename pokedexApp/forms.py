from django import forms
from .models import TeamModel

class TeamForm(forms.ModelForm):

    class Meta:
        model = TeamModel
        fields = ['name', 'pokemon1', 'pokemon2', 'pokemon3', 'pokemon4', 'pokemon5',]