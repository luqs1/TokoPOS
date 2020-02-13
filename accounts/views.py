from django.shortcuts import render


def index(request):
    return render(request, 'base.html')  # temporary until index is developed.
