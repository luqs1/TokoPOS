from accounts import models
from django.utils import timezone


class SessionEvent(models.SessionEventModel):  # goes in Django Session, and creates Session Events when saved.
    def __init__(self, **kwargs):  # child initialisation
        super().__init__(**kwargs)  # initialises like parent first to get django model features working.
        self._active = True  # private; on creation, the Event should be considered active. subject to change.
        self._access = {'self': self.staff}  # private; W.I.P; the access dictionary is created based on self.staff

    @property  # _active should definitely be freely accessible.
    def active(self):
        return self._active

    @active.setter  # Only allows _active to be set to a boolean value.
    def active(self, state):
        if type(state) == bool:
            self._active = state
        else:
            raise TypeError

    @property  # _access only has a getter and no setter, as it shouldn't be set from outside of this class.
    def access(self):
        return self._access

    @property
    def login_time(self):  # login time should be freely accessible according to documentation.
        return self._login_time

    @login_time.setter  # only allows later times to be added, thinking of changing this so that it can't be changed.
    def login_time(self, new_login_time):
        if type(new_login_time) == timezone.timezone:
            if new_login_time > self._login_time:
                self._login_time = new_login_time
            else:
                raise ValueError
        else:
            raise TypeError

    @property  # current design choice was to make logout time inaccessible, might change that.
    def logout_time(self):
        raise RuntimeError

    @logout_time.setter  # does as the login_time setter.
    def logout_time(self, new_logout_time):
        if type(new_logout_time) == timezone.timezone:
            if new_logout_time > self._logout_time:
                self._logout_time = new_logout_time
            else:
                raise ValueError
        else:
            raise TypeError

    def update(self):  # shouldn't be directly called, works inside save.
        if hasattr(self, '_login_time') and hasattr(self, '_logout_time'):
            self._duration_hours = self._logout_time - self.login_time  # inbuilt conversion to timedelta from timezone.
        else:
            raise RuntimeError  # shouldn't update without a login and logout time.

    def save(self, **kwargs):  # extends the normal model save method, updates the duration before doing as per normal.
        self.update()
        super().save(**kwargs)  # kwargs are to retain functionality.
