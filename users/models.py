from django.db import models
from core.settings import FRONT_URL
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField

from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string

from django_rest_passwordreset.signals import reset_password_token_created


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


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token,
                                 *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'site_name': "PupCrawlApp.com",
        'email': reset_password_token.user.email,
        'reset_password_url':
            FRONT_URL + "/PasswordReset/{}".format(reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('emails/user_reset_password.html',
                                          context)
    email_plaintext_message = \
        render_to_string('emails/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@centribaltest.com",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()



