from django import forms
from . import models


class TournamentCreationForm(forms.Form):

    class Meta:
        model = models.TournamentsList
        fields = ['title', 'slug', 'body', 'logo']