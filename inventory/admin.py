from django.contrib import admin
from inventory import models

MODELS = [models.Category,
          models.ProductsIngredient,
          models.Product,
          models.Ingredient,
          ]
for MODEL in MODELS:
    admin.site.register(MODEL)
