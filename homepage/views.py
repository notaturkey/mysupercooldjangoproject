from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

class MyException(Exception):
    pass

def index(request):
    return render(request, 'homepage/index.html')

def account(request):
    return render(request, 'homepage/account.html')

def user(request, userName):
    return render(request, 'homepage/user.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['inputUser']
        password = request.POST['inputPass']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            auth_login(request, user)
            return redirect('index')
        else:
            # No backend authenticated the credentials
            messages.error(request,'username or password not correct')
            return redirect('login')
    
    return render(request, 'homepage/login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['inputEmail']
        username = request.POST['inputUser']
        password = request.POST['inputPass']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'username is taken, try another')
            return redirect('signup')
        
        user = User.objects.create_user(username,email=email, password=password)
        user.save()
        messages.error(request,'Account Created, Thanks for signing up!')
        return render(request, 'homepage/index.html')

    return render(request, 'homepage/signup.html')

def thanks(request):
    return render(request, 'homepage/thanks.html')

def logout(request):
    auth_logout(request)
    messages.error(request,'Logged Out')
    return redirect('index')
