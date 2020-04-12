from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']

def index(request):
    return render(request, 'authenticate/index.html')

def login(request):
    return render(request, 'authenticate/login.html')

def send(request):
    return render(request, 'authenticate/send.html')

def receive(request):
    gender = request.POST['gender']
    print(gender)
    return render(request, 'authenticate/receive.html', {'gender': gender})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('authenticate:index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('authenticate:login')
    else:
        return redirect('authenticate:login')
