from django.db import models
from django.contrib.auth.models import User  # This is the User model from django's default authentication.
from django.utils import timezone


class Staff(models.Model):  # This creates the Staff table in my SQLite database.
    FEMALE = 'F'
    MALE = 'M'
    id = models.AutoField(primary_key=True)  # this is done automatically, but I included it to mention that explicitly.
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1to1 relationship with the User's table/ relation.
    # The CASCADE method means that if a User record is deleted, the Staff record will also be deleted.
    sex = models.CharField(max_length=1,
                           choices=[
                               (MALE, 'Male'),
                               (FEMALE, 'Female')
                           ])  # either M or F is stored in the database.
    first_name = models.CharField('First Name', max_length=15)
    last_name = models.CharField('Last Name', max_length=15)
    email = models.EmailField(max_length=50, unique=True)  # a CharField that verifies with an Email Validator.
    phone_number = models.IntegerField('National Phone Number')  # The name of the field should be informative enough.

    def __str__(self):  # string representation of the object, should be the first name.
        return self.first_name + self.last_name


"""
User model contains:
username
password
email
first_name
last_name
,
therefore I commented out both the name and email fields initially, however as they are not required fields I have made
them fields in the Staff instead rather than editing the user model.

Passwords are hashed before being stored, which I'll get into later.
"""


class SessionEventModel(models.Model):  # the model that will create the record in the Database.
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)  # if Staff record deleted, delete Session Events from it
    _login_time = models.DateTimeField('Login Time', default=timezone.now)  # the function shouldn't be run for default.
    # or could use auto_now_add to make it non-editable
    _logout_time = models.DateTimeField('Logout Time', default=timezone.now)  # as a reference to compare later logout
    _duration_hours = models.DurationField('Duration (Hours)')  # time delta, from datetime module
    # private variables are used so that the extended class can create setters and getters.


class Role(models.Model):  # alias for access
    name = models.CharField(max_length=15)
    creator_id = models.CharField(max_length=2)


class StaffRole(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    authoriser_id = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='+')
    # doesn't delete itself if auth del.

    class Meta:
        unique_together = (('staff_id', 'role_id'),)  # makes them act like p.keys.


class App(models.Model):
    name = models.CharField(max_length=15)


class RolesApp(models.Model):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    app_id = models.ForeignKey(App, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('role_id', 'app_id'),)  # surrogate to make them both act like two p. keys

