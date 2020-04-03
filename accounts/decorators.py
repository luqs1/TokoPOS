from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # allows me to make login required inside my decorator
"""
APPS = {'CASHIER': 1,
        'CHEF': 2,
        'REPORTING': 3,
        'STAFF': 4,
        }
deprecated
"""
# from page navigation design, these are the different apps one can be authorised for.


def authorisation_constructor(app):  # returns a partial function which is used as a decorator

    def authorise(view):  # the decorator

        @login_required  # so my authorised view is also a login required view.
        def authorised_view(request):  # takes a request because the decorator only works on views
            users_apps = request.session['SessionEvent']['access']  # due to login required, this will exist.
            if app in users_apps:  # checking if the app is one accessible to the user
                return view(request)  # and if so returns the view that was decorated
            return render(request, 'accounts/index.html',
                          context={'message': "You aren't authorised to access that app",
                                   'loggedIn': True})
            # otherwise returns them to the index page without the login feature.
        return authorised_view  # this is the result of the partial function decorator
    return authorise  # this is what is returned when used to create the partial function


"""
Usage would be as such:
from accounts.decorators import authorisation_constructor
for_cashiers = authorisation_constructor('CASHIER')

@for_cashiers
def some_view(request):
    ...

note that @login_required is never required as it is a part of the decorator.
Changing the functionality to authorise non-staff only requires the removal of @login_required from the code.
"""
