from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Products(models.Model):

    reference = models.CharField(max_length=20)

    name = models.CharField(max_length=30)

    description = models.TextField()

    price = models.DecimalField(max_digits=12, decimal_places=2)

    tax = models.DecimalField(max_digits=4, decimal_places=2)

    stock = models.IntegerField(default=0,)

    status = models.BooleanField(default=True, verbose_name=_('Status'))

    history = HistoricalRecords()

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))

    modified_date = models.DateTimeField(default=timezone.now,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')




