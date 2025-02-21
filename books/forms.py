from django import forms
from . import models

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = models.ReviewModel
        fields = '__all__'