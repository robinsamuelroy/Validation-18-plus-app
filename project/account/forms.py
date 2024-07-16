from datetime import date
from django import forms
from .models import *

class UserForm(forms.ModelForm):
  date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])

  class Meta:
    model = User
    fields = ['username','email','password','date_of_birth']

  def clean_date_of_birth(self):
    dob = self.cleaned_data['date_of_birth']
    today = date.today()
    age = today.year - dob.year - ((today.month,today.day)<(dob.month,dob.day))
    if age<18:
      raise forms.ValidationError("18+ only allowed")
    return dob