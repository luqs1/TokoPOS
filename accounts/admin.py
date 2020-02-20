from django.contrib import admin
from accounts import models

# Register your models here.
admin.site.register(models.Staff)  # will allow Staff to be registered on the admin site.
admin.site.register(models.SessionEventModel)  # temporary, just so I can debug.
