from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'correo@ejemplo.com'
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre de usuario'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Mínimo 8 caracteres'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmar contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def clean_password1(self):

        password = self.cleaned_data.get('password1')

        if len(password) < 8:

            raise ValidationError(
                'La contraseña debe tener mínimo 8 caracteres.'
            )

        if password.isnumeric():

            raise ValidationError(
                'La contraseña no puede estar compuesta únicamente por números.'
            )

        return password

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password1")
        username = cleaned_data.get("username")

        if password and username:

            if username.lower() in password.lower():

                self.add_error(
                    "password1",
                    "La contraseña es demasiado similar al nombre de usuario."
                )

        return cleaned_data