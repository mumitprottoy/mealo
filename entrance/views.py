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
    
    if request.method=='POST':
        user, pwd = getUser(request.POST['username']), request.POST['password'] 
        if not bool(user):
            context['err_msg']=bool_message(msg='Username or email does not exist.', type=False)
        elif not bool(authenticate(username=user.username, password=pwd)):
            context['username']=str(user.username)
            context['err_msg']=bool_message(msg='Wrong password.', type=False)
        else:
            enter(request, user)
            return redirect('landing')

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


