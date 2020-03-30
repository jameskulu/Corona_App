from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    country_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Search country',
        'class': 'input',
        'autocomplete': 'off'
    }))

    class Meta:
        model = Country
        fields = '__all__'
