from accounts import models
from django.utils import timezone


class SessionEvent(models.SessionEventModel):  # goes in Django Session, and creates Session Events when saved.
    def __init__(self, **kwargs):  # child initialisation
        kwargs = self.filter_kwargs(kwargs)
        super().__init__(**kwargs)  # initialises like parent first to get django model features working.

    def filter_kwargs(self, kwargs):
        if 'staff' in kwargs.keys():
            kwargs['staff'] = models.Staff.objects.get(id=kwargs['staff'])  # to get Staff model object for the SE model
        if 'access' in kwargs.keys():  # if access has already been given
            self._access = kwargs['access']
            del kwargs['access']  # access is not a part of the SE model, so it is removed from the kwargs.
        else:  # the access wasn't provided and a call to the database is required.
            self._access = []  # private
        return kwargs

    @property  # _access only has a getter and no setter, as it shouldn't be set from outside of this class.
    def access(self):
        return self._access

    @property
    def login_time(self):  # login time should be freely accessible according to documentation.
        return self._login_time

    @login_time.setter  # only allows later times to be added, thinking of changing this so that it can't be changed.
    def login_time(self, new_login_time):
        if type(new_login_time) == timezone.datetime:
            self._login_time = new_login_time
        else:
            raise TypeError

    @property  # current design choice was to make logout time inaccessible, might change that.
    def logout_time(self):
        raise RuntimeError

    @logout_time.setter  # does as the login_time setter.
    def logout_time(self, new_logout_time):
        if type(new_logout_time) == timezone.datetime:
            self._logout_time = new_logout_time
        else:
            raise TypeError

    def update(self):  # shouldn't be directly called, works inside save.
        if hasattr(self, '_login_time') and hasattr(self, '_logout_time'):
            self._duration_hours = self._logout_time - self.login_time  # inbuilt conversion to timedelta from timezone.
        else:
            raise RuntimeError  # shouldn't update without a login and logout time.

    def data(self):  # creates a serializable data output to put in the session
        output = {
            'login_time': self._login_time.isoformat(),
            'access': self.access,
            'staff': self.staff_id  # this is specifically the staff id so that staff data isn't available on the cookie
        }
        return output

    def save(self, **kwargs):  # extends the normal model save method, updates the duration before doing as per normal.
        self.update()
        super().save(**kwargs)  # kwargs are to retain functionality.
