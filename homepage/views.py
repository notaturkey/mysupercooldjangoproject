from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as LG
from django.contrib.auth.models import User

from .forms import UserForm

def index(request):
    template = loader.get_template('homepage/index.html')
    context = {}
    if not request.user.is_authenticated:
        pass
    return HttpResponse(template.render(context, request))

def user(request, uname):
    pass

def login(request):
    template = loader.get_template('homepage/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

class MyException(Exception):
    pass

def signup(request):
    template = loader.get_template('homepage/signup.html')
    context = {}
    if request.method == 'POST':
        email = request.POST['inputEmail']
        username = request.POST['inputUser']
        password = request.POST['inputPass']
        password2 = request.POST['inputPass2']

        print(email)
        print(username)
        print(password)
        print(password2)
        
        user = User.objects.create_user(username,email=email, password=password)
        user.save()
        


    return HttpResponse(template.render(context, request))

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        LG(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
