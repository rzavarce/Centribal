from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField

TYPE_USER = ((1, _('Administrator')), (2, _('Editor')), (3, _('Consulter')))

class UserProfile(AbstractUser):

    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    address = models.CharField(max_length=255, verbose_name=_('Address'),
                               blank=True, null=True)

    zip_code = models.IntegerField(verbose_name=_('Zip Code'),
                                   blank=True, null=True)

    birth_date = models.DateField(verbose_name=_('Birth Date'), blank=True,
                                  null=True)

    phone_number = PhoneNumberField(verbose_name=_('Phone Number'), blank=True,
                                    null=True)

    type_user = models.IntegerField(choices=TYPE_USER,
                                    verbose_name=_('Type User'), default=1)

    status = models.BooleanField(default=True, verbose_name=_('Status'))

    history = HistoricalRecords()

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))

    modified_date = models.DateTimeField(default=timezone.now,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
