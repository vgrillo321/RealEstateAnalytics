from django import forms

class CityStateForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    state = forms.CharField(label='State', max_length=2)