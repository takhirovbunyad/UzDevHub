from django import forms
from .models import Projects

class Pro_form(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
