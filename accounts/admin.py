from django.contrib import admin
from accounts import models

# Register your models here.
MODELS = [
    models.Staff,  # will allow Staff to be registered on the admin site.
    models.Role,  # allows Roles to be added
    models.StaffRole,  # allows Roles to be tied to Staff members
    models.App,  # allows Apps to be set up
    models.RolesApp,  # allows Roles to be tied with Apps.
]
for MODEL in MODELS:
    admin.site.register(MODEL)
