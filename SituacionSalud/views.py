from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    return render(request,'situacionsalud/index.html/',{'variable':'asdasdasdasds'})

def login (request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        if action == 'login':
            redirect('situacionsalud/index.html/')
    return render(request, 'situacionsalud/login.html', {'variable': 'asdasdasdasds'})

def factorescondicionantes (request):
    return render(request,'situacionsalud/factorescondicionantes.html/',{'variable':'asdasdasdasds'})