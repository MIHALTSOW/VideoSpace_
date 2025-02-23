from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from pygments.lexer import default

from .models import User, Profile


class RegistrationForm(forms.ModelForm):
    """ Registration form. """
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """ Login form. """
    username = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UpdatePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = []


class UpdateProfileForm(forms.ModelForm):
    """ Update profile form. """

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'sex', 'age', 'telegram']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'rows': 1}),
        }
