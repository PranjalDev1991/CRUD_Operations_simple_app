from django import forms
from crud.models import crudst

class stforms(forms.ModelForm):
    class Meta:
        model=crudst
        fields="__all__"
