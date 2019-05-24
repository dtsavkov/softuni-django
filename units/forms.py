from django import forms
from django.core.validators import MinValueValidator

from .models import Units, UnitType


class UnitTypeForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(                           # HTML field type
        attrs={
            'class': 'form-control'                                                         # Bootstrap formatting
        }))

    class Meta:
        model = UnitType
        fields = ('id', 'name',)


class CreateUnitForm(forms.ModelForm):
    make = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    model = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    price = forms.IntegerField(required=True,
                               validators=[MinValueValidator(10)],
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control',
                                          'type': 'number'
                                          }
                               ))

    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    type = forms.ModelChoiceField(queryset=UnitType.objects.all(),
                                  widget=forms.Select(
                                      attrs={'class': 'form-control'}
                                  ))

    # material field should be select field, which list all materials from table Material

    class Meta:
        model = Units
        fields = ('id', 'make', 'model', 'description', 'price', 'image_url', 'type',)

