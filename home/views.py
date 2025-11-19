from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password



def show_home_page(request: HttpRequest):
    if request.COOKIES.get('email') is None:
        return redirect('/users/login')
    
    return render(request, 'home.html')

# Create your views here.
