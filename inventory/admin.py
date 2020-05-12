from django.contrib import admin
from inventory import models

MODELS = [models.Category,
          models.ProductsIngredient,
          models.Product,
          models.Ingredient,
          models.TransactionsList,
          models.Transaction,
          ]
for MODEL in MODELS:
    admin.site.register(MODEL)
