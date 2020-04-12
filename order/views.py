from django.shortcuts import render, redirect
from .models import Week, Menu, Food, Starter, MainCourse, Dessert
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'order/index.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        floor = request.POST['floor']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username is taken. Try another.')
                return redirect('order:register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name)
                user.save()
                return redirect('order:register')
        else:
            messages.info(request, "Those passwords didn't match. Try again.")
            return redirect('order:register')

    return render(request, 'order/register.html')
