from  django import forms
from .models import Rentall

class RentallForm(forms.ModelForm):
  address=forms.CharField(label='')
  class Meta:
   model=Rentall
   fields=['address']