from django import forms
from . import models

class TodoOrderForm(forms.ModelForm):
    class Meta:
        model = models.CartModel
        fields = '__all__'