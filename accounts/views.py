from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegistroUsuarioForm


def registro(request):

    if request.method == 'POST':

        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Cuenta creada correctamente. Ahora puedes iniciar sesión.'
            )

            return redirect('login')

    else:

        form = RegistroUsuarioForm()

    return render(
        request,
        'accounts/registro.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('categorias')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            User.objects.get(username=username)

        except User.DoesNotExist:

            messages.error(
                request,
                'El usuario no existe. Debes registrarte primero.'
            )

            return render(
                request,
                'accounts/login.html'
            )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:

            messages.error(
                request,
                'La contraseña ingresada es incorrecta.'
            )

            return render(
                request,
                'accounts/login.html'
            )

        login(
            request,
            user
        )

        return redirect('categorias')

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Has cerrado sesión correctamente.'
    )

    return redirect('inicio')