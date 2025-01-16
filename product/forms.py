from django import forms
from django.forms import ModelForm

from .models import Product

class ProductForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'enter product name'}))
    product_name = forms.TimeField(widget=forms.TextInput(attrs={'placeholder':'enter product description'}))
    product_name = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'enter product Price'}))
    product_name = forms.CheckboxInput()

    class Meta:
        model = Product
        fields = "__all__"

