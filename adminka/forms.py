from django import forms
from adminka.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'category': forms.TextInput(attrs={'class': 'category'}),
            'price': forms.NumberInput(attrs={'class': 'price'})
        }
