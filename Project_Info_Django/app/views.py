
# Create your views here.
from django.shortcuts import render, redirect
from .models import Alumno, Nota, Asistencia
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')