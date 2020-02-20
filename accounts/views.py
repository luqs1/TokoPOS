from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout  # the authentication function within Django
from django.http import HttpResponseRedirect  # let's me send the
from django.urls import reverse  # synonymous to {% url 'argument'%} but in views instead of templates.
from django.contrib.auth.decorators import login_required  # decorator to verify login
from accounts import classes as my
from accounts import models


def index(request):
    if request.method == 'POST':  # if the form was submitted
        username = request.POST.get('username')  # username from form
        password = request.POST.get('password')  # password from form

        user = authenticate(username=username, password=password)  # returns True if authenticated and more.
        if user:
            if user.is_active:  # if Django deems that this user is active, says it's successful.
                login(request, user)  # ties the user to the session with cookies.
                request.session['SessionEvent'] = my.SessionEvent(staff=models.Staff(user=request.user))
                print(request.session['SessionEvent'])
                return render(request, 'accounts/index.html', context={'message': 'Login Successful'})
            else:  # Account was inactive but authenticated.
                return render(request, 'accounts/index.html', context={'message': 'Account was not active'})
        else:  # Account wasn't authenticated, try again.
            return render(request, 'accounts/index.html', context={'message': 'Login failed, please try again.'})
    return render(request, 'accounts/index.html')  # Method wasn't POST, presents the normal index page.


@login_required  # Decorates the function with a built-in function that checks to see if a user was logged in first.
def staff_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))