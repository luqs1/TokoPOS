from django.db import models
from django.contrib.auth.models import User  # This is the User model from django's default authentication.


class Staff(models.Model):  # This creates the Staff table in my SQLite database.
    FEMALE = 'F'
    MALE = 'M'
    id = models.AutoField(primary_key=True)  # this is generally done automatically, but I included it explicitly here.
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1to1 relationship with the User's table/ relation.
    # The CASCADE method means that if a User record is deleted, the Staff record will also be deleted.
    sex = models.CharField(max_length=1,
                           choices=[
                               (MALE, 'Male'),
                               (FEMALE, 'Female')
                           ])  # either M or F is stored in the database.
    # name = models.CharField(max_length=15)
    # email = models.EmailField(max_length=50)  # a CharField that verifies it's an email with an Email Validator.
    phone_number = models.IntegerField('National Phone Number', max_length=11)  # max_length of 11 forces national no.


"""
User model requires/ contains:
username
password
email
first_name
last_name
,
therefore I commented out both the name and email fields.

Passwords are hashed before being stored, which I'll get into later.
"""