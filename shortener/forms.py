from django import forms

from .models import ShortURL


class URLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = '__all__'
