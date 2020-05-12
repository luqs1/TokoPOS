from django.db import models
from accounts import models as a_models


class Ingredient(models.Model):  # Any ingredient is added here, it can be measured by mass or quantity.
    name = models.CharField(max_length=30)
    mass_measured = models.BooleanField('Amount as Mass')
    amount = models.FloatField(auto_created=True, default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):  # product, with boolean for whether the product is producible in-store
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    producible = models.BooleanField('Produced in-store')
    quantity = models.IntegerField(auto_created=True, default=0)
    price = models.FloatField('Price (£)')

    def __str__(self):
        return self.name + ' ' + str(self.category)


class ProductsIngredient(models.Model):  # is ready to calculate the statistical value of the ingredient used to cook.
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount_mean = models.FloatField(auto_created=True, default=0)
    amount_sd = models.FloatField(auto_created=True, default=0)
    sample_size = models.IntegerField(auto_created=True, default=0)

    class Meta:  # simulates composite p.key behaviour
        unique_together = (('ingredient', 'product'),)

    def __str__(self):
        return str(self.product) + ':' + str(self.ingredient)


class Transaction(models.Model):
    customer = models.CharField(max_length=20)
    server = models.ForeignKey(a_models.Staff, on_delete=models.SET_NULL, null=True)
    total = models.FloatField('Total (£)', blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()

    def __str__(self):
        return ': '.join([self.customer, str(self.server), str(self.total), self.datetime.day])


class TransactionsList(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    subtotal = models.FloatField('Subtotal (£)',)

    def __str__(self):
        return ' '.join([str(self.product), str(self.quantity)])
