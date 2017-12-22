from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from pip.cmdoptions import no_binary

from .models import *
from .models import SituacionSalud
from .forms import *


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
    return render(request, 'situacionsalud/factorescondicionantes.html', {'variable': 'asdasdasdasds'})


def reportnivelsalud(request):
    return render(request, 'situacionsalud/reportnivelsalud.html', {'variable': 'asdasdasdasds'})


def NSr1(request):
    return render(request, 'situacionsalud/NSr1.html', {'variable': 'asdasdasdasds'})


def NSr2(request):
    return render(request, 'situacionsalud/NSr2.html', {'variable': 'asdasdasdasds'})


def NSr3(request):
    return render(request, 'situacionsalud/NSr3.html', {'variable': 'asdasdasdasds'})


def NSr4(request):
    return render(request, 'situacionsalud/NSr4.html', {'variable': 'asdasdasdasds'})


def NSr5(request):
    return render(request, 'situacionsalud/NSr5.html', {'variable': 'asdasdasdasds'})


def NSr6(request):
    return render(request, 'situacionsalud/NSr6.html', {'variable': 'asdasdasdasds'})


def NSr7(request):
    return render(request, 'situacionsalud/NSr7.html', {'variable': 'asdasdasdasds'})


def NSr8(request):
    return render(request, 'situacionsalud/NSr8.html', {'variable': 'asdasdasdasds'})


def reportfactorescondicionantes(request):
    return render(request, 'situacionsalud/reportfactorescondicionantes.html', {'variable': 'asdasdasdasds'})


def FCr1(request):
    return render(request, 'situacionsalud/FCr1.html', {'variable': 'asdasdasdasds'})


def FCr2(request):
    return render(request, 'situacionsalud/FCr2.html', {'variable': 'asdasdasdasds'})


def FCr3(request):
    return render(request, 'situacionsalud/FCr3.html', {'variable': 'asdasdasdasds'})


def NSf1(request):
    form = SituacionSaludForm()
    try:
        if request.method == 'POST':
            form = SituacionSaludForm(request.POST)
            if form.is_valid():
                situasionsalud = form.save(commit=False)
                edd = request.POST.get('edad')
                if 0 <= int(edd) <= 29:
                    edad_o = Edad(edad=int(edd), tipo='D', nomenclaturar='Dias')
                if 51 <= int(edd) <= 61:
                    edad_o = Edad(edad=int(edd), tipo='M', nomenclaturar='Meses')
                if 100 <= int(edd):
                    edad_o = Edad(edad=int(int(edd) - 100), tipo='A', nomenclaturar='Años')

                edad_o.save()
                situasionsalud.edad = edad_o
                situasionsalud.save()
                form.save_m2m()
    except Exception:
        print('salior error')

    return render(request, 'situacionsalud/FCf1.html', {'form': form})


def FCf1(request):
    form = FactoresCondicionantesForm()
    try:
        if request.method == 'POST':
            form = FactoresCondicionantesForm(request.POST)
            if form.is_valid():
                poblacion = form.save(commit=False)
                poblacion.save()
               # form.save_m2m()
    except Exception:
        print('salior error')

    return render(request, 'situacionsalud/FCf1.html', {'form': form})


def reportes(request):
    return render(request, 'situacionsalud/reportes.html', {'variable': 'asdasdasdasds'})


def report(request):
    return render(request, 'situacionsalud/report.html', {'variable': 'asdasdasdasds'})


def ingresardatos(request):
    form = SituacionSaludForm()
    return render(request, 'situacionsalud/ingresardatos.html', {'form': form})


import csv
import os
from django.conf import settings

path_cie = os.path.join(settings.BASE_DIR, 'static/cie.csv')
path_distr = os.path.join(settings.BASE_DIR, 'static/distrito.csv')
path_esta = os.path.join(settings.BASE_DIR, 'static/EstablecimientoSalud.csv')
path_situacion = os.path.join(settings.BASE_DIR, 'static/situacionsalud.csv')


def migrar_cie():
    try:
        ob = Cie.objects.all().delete()
        url = path_cie
        with open(url) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for i in entrada:
                cod, desc = i
                cie = Cie(codigo=str(cod).strip().upper(),
                          descripcion=str(desc).strip())
                cie.save()

    except Exception:
        print('error cie')


def migrar_sexo():
    try:
        ob = Sexo.objects.all().delete()
        sf = Sexo(nombre='Masculino', abreviacion='M')
        sf.save()
        sm = Sexo(nombre='Femenino', abreviacion='F')
        sm.save()
    except Exception:
        print('error')


def migrar_distrito():
    try:
        ob = Distrito.objects.all().delete()
        url = path_distr
        with open(url) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for i in entrada:
                cod, num = i
                cie = Distrito(nombre=str(cod).strip())
                cie.save()

    except Exception:
        print('error distrito')


def migrar_establecimiento():
    try:
        ob = EstablecimientoSalud.objects.all().delete()
        url = path_esta
        with open(url) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for i in entrada:
                ID, EESS = i
                cie = EstablecimientoSalud(codigo=str(ID).strip().upper(),
                                           descripcion=str(EESS).strip())
                cie.save()

    except Exception:
        print('error EstablecimientoSalud')


def migrar_situacionsalud():
    try:
        ob = SituacionSalud.objects.all().delete()
        url = path_situacion
        with open(url) as csvarchivo:
            entrada = csv.reader(csvarchivo)
            for i in entrada:
                id, persons, edd, cod, sex, distrit = i

                if 0 <= int(edd) <= 29:
                    edad_o = Edad(edad=int(edd), tipo='D', nomenclaturar='Dias')
                if 51 <= int(edd) <= 61:
                    edad_o = Edad(edad=int(edd), tipo='M', nomenclaturar='Meses')
                if 100 <= int(edd):
                    edad_o = Edad(edad=int(int(edd) - 100), tipo='A', nomenclaturar='Años')

                edad_o.save()

                ees_o = EstablecimientoSalud.objects.filter(codigo=str(id).strip().upper()).first()
                cie_o = Cie.objects.filter(codigo=str(cod).strip().upper()).first()
                distrit_o = Distrito.objects.filter(nombre=str(distrit).strip()).first()
                sex_o = Sexo.objects.filter(abreviacion=str(sex).strip().upper()).first()

                situsal = SituacionSalud(eess=ees_o, cie=cie_o, distrito=distrit_o, sexo=sex_o, edad=edad_o)
                # print(situsal)
                situsal.save()

    except Exception:
        print('error SituacionSalud')
