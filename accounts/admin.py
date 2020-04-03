from django.contrib import admin
from accounts import models as a_models  # accounts models
from inventory import models as i_models  # inventory models

# Register your models here.
MODELS = [
    a_models.Staff,  # will allow Staff to be registered on the admin site.
    a_models.Role,  # allows Roles to be added
    a_models.StaffRole,  # allows Roles to be tied to Staff members
    a_models.App,  # allows Apps to be set up
    a_models.RolesApp,  # allows Roles to be tied with Apps.
    i_models.Product,  # allows all to be added by the Chef.
    i_models.Ingredient,
    i_models.ProductsIngredient,
    i_models.Category,
]
for MODEL in MODELS:
    admin.site.register(MODEL)
