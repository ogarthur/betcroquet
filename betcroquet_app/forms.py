from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from betcroquet_app.models import Bet
from django.core.files.images import get_image_dimensions

class AddBetForm(forms.Form):
    gameCode = forms.CharField(widget = forms.TextInput(attrs={'required':'required','class':'form-control',}))

    def clean(self):
        all_clean_data = super( AddBetForm,self).clean()
        gameCode    = all_clean_data['gameCode']
