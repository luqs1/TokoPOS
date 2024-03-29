"""TokoPOS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views  # this is the only app for which the views will be directly in the main urls.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.staff_logout, name='logout'),
    path('manager_test', views.manager_test),
    path('', views.index, name='index'),  # due to the accounts import, now the index is a project level view.
]
