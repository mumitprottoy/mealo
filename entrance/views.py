from django.contrib.auth import authenticate, login as enter
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from subroutines.decorators import auth_check
from subroutines.meal_messages import bool_message
from subroutines.userObject import getUser
from django.db.models import Q





def landing(request):
    return render(request, 'entrance/landing.html', {})




@auth_check
def login(request):
    htm = 'entrance/login.html'
    context = {
        'title': 'Login',
    }
    return render(request, htm, context)



@auth_check
def signup(request):
    htm = 'entrance/signup.html'
    context = {
        'title': 'Signup'
    }
    return render(request, htm, context)



@auth_check
def forgot_password(request):
    htm = 'entrance/forgot_password.html'
    context = {
        'title': 'Forgot Password'
    }
    return render(request, htm, context)


