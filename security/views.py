from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registerpage(request):
    if request.user.is_authenticated:
        return redirect ('index')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')


    token = get_token(request)
    template = 'reg.html'
    context = {'form': form }
    return render(request, template, context)


def home(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username = username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
    template = 'log.html'
    context = {}
    return render(request, template, context)


def Userlogout(request):
    logout(request)
    return redirect('login')



def service(request):
    template = 'service.html'
    return render(request, template)


def contact(request):
    template = 'contact.html'
    return render(request, template)

def Aboutus(request):
    template = 'about.html'
    return render(request, template)

def Myacount(request):
    template = 'form.html'
    return render(request, template)
