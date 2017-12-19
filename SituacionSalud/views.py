from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def authentication(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            user = authenticate(username=username,
                                password=password)
            login(request, user)
            return redirect('/')
        except Exception:
            pass
    return render(request, 'situacionsalud/login.html', {})


@login_required
def index(request):
    return render(request, 'situacionsalud/index.html', {})


def factorescondicionantes(request):
    return render(request, 'situacionsalud/factorescondicionantes.html/', {'variable': 'asdasdasdasds'})

def reportes(request):
    return render(request, 'situacionsalud/reportes.html/', {'variable': 'asdasdasdasds'})

def report(request):
    return render(request, 'situacionsalud/report.html/', {'variable': 'asdasdasdasds'})