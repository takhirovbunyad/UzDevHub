from django import forms
from .models import Projects

class Pro_form(forms.ModelForm):
    class Meta:
        model = Projects
        fields = [
            'owner_name',
            'owner_last_name',
            'title',
            'code',
            'url',
            'description',
            'file',
            'category',
            'status',
        ]