from cProfile import label
from django import forms
from .models import Flower

class MyForm(forms.ModelForm):
    title = forms.CharField(label="Title:", widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(label="Description", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Flower
        fields = [
            'title',
            'description',                     #represent the field in the form
        ]