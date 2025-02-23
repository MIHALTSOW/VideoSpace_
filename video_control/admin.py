from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .models import Video, Photo, User, Profile


class EmailAuthenticationForm(AuthenticationForm):
    """ Переопределяет метод clean, чтобы проверять пароль и email пользователя"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Email'

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = get_user_model().objects.filter(email=email).first()
            if self.user_cache and self.user_cache.check_password(password):
                return self.cleaned_data
            else:
                raise forms.ValidationError('Неправильный email или пароль')
        return self.cleaned_data


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'updated_at')
    readonly_fields = ('slug',)
    exclude = ('user_permissions',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(Photo)
admin.site.login_form = EmailAuthenticationForm
