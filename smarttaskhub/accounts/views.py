from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegisterForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
def login_view(request):
    form = loginForm()
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/Login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully")
            return redirect('login')
    return render(request, 'accounts/Register.html', {'form': form})
@login_required
def home_view(request):
    return HttpResponse(f"Welcome to Home Page! {request.user}")
