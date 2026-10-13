from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import CustomUserCreationForm


def signup(request):
    if request.user.is_authenticated:
        return redirect('all_recipes')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('all_recipes')
    else:
        form = CustomUserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('all_recipes')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('all_recipes')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('login')