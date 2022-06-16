from django import forms
from movie.models import Moviemodel

class Movieform(forms.ModelForm):

    class Meta:
        model=Moviemodel
        fields='__all__'
