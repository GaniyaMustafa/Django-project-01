from django.shortcuts import render
from .forms import LoginForm
from django.views.generic import ListView
from . import models
from django.http import HttpResponseRedirect
log = False

def index(request):
    login_form = LoginForm(request.POST or None)
    global log
    context = {
        'login_form' : login_form,
    }

    log = False
    
    return render(request, 'login/index.html', context)

def login(request):
    
    data = models.login.objects.all()
    username = 'null'
    password = 'null'
    global log

    login_form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

    for d in data:
        if username == d.username and password == d.password:
            log = True
            return HttpResponseRedirect('kategori/')
        else:
            log = False
            return HttpResponseRedirect('/')
