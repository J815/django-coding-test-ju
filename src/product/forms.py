from django.forms import forms, ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput
from django import forms

from product.models import Variant


class VariantForm(ModelForm):
    class Meta:
        model = Variant
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'active'})
        }


class ProductFilterForm(forms.Form):
    title = forms.CharField(required=False)
    variant = forms.CharField(required=False)
    price_from = forms.DecimalField(required=False, min_value=0)
    price_to = forms.DecimalField(required=False, min_value=0)
    date = forms.DateField(required=False)
