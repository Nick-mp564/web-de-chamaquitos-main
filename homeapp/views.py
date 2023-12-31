from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")


def signup(request):

    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
             })
    
    else:
        if request.POST["password1"] == request.POST["password2"]:
            #reguster user
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("inicio")
            except IntegrityError:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "username already exists"
                    })
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "Password do not match"
            })

@login_required    #no cualquera lo puede hacceder entonces por eso se le coloca esa @, es para proteger el citio 
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home') 


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
            })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('inicio')
@login_required
def afectados(request):
    return render(request, 'afectados.html')

@login_required
def paisajes(request):
    return render(request, 'paisajes.html')