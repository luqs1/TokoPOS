from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout  # the authentication function within Django
from django.http import HttpResponseRedirect  # let's me send the
from django.urls import reverse  # synonymous to {% url 'argument'%} but in views instead of templates.
from django.contrib.auth.decorators import login_required  # decorator to verify login
from accounts import classes as my
from accounts import models
from django.utils import timezone
from accounts.decorators import authorisation_constructor

managers_only = authorisation_constructor('STAFF')


def index(request):
    if request.method == 'POST':  # if the form was submitted
        username = request.POST.get('username')  # username from form
        password = request.POST.get('password')  # password from form

        user = authenticate(username=username, password=password)  # returns True if authenticated and more.
        if user:
            if user.is_active:  # if Django deems that this user is active, says it's successful.
                login(request, user)  # adds the user to the session on cookies.
                staff_id = models.Staff.objects.get(user_id=request.user.id).id
                event = my.SessionEvent(staff=staff_id)
                request.session['SessionEvent'] = event.data()
                print(request.session['SessionEvent'])
                return render(request, 'accounts/index.html', context={'message': 'Login Successful', 'loggedIn': True})
            else:  # Account was inactive but authenticated.
                return render(request, 'accounts/index.html', context={'message': 'Account was not active'})
        else:  # Account wasn't authenticated, try again.
            return render(request, 'accounts/index.html', context={'message': 'Login failed, please try again.'})
    return render(request, 'accounts/index.html')  # Method wasn't POST, presents the normal index page.


@managers_only
def manager_test(request):
    return render(request, 'accounts/index.html', context={'message': 'You are indeed a manager.', 'loggedIn': True})


@login_required  # Decorates the function with a built-in function that checks to see if a user was logged in first.
def staff_logout(request):
    arguments = request.session['SessionEvent']
    arguments['login_time'] = timezone.datetime.fromisoformat(arguments['login_time'])  # converts back to datetime obj
    event = my.SessionEvent(**arguments)
    event.logout_time = timezone.now()
    event.save()
    logout(request)
    return HttpResponseRedirect(reverse('index'))
