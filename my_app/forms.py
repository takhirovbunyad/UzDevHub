from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Projects, CustomUser


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

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Bu email manzil oldin ro'yxatdan o'tgan.")
        return email