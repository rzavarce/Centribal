import uuid
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


class OrderDetail(models.Model):

    order = models.ForeignKey('orders.Orders', on_delete=models.CASCADE)

    product = models.ForeignKey('products.Products', on_delete=models.PROTECT)

    quantity = models.IntegerField()


class Orders(models.Model):

    reference = models.UUIDField(default=uuid.uuid4, )

    order_detail = models.ManyToManyField('products.Products',
                                          through=OrderDetail)

    price_total = models.DecimalField(max_digits=22, decimal_places=2)

    price_total_tax = models.DecimalField(max_digits=22, decimal_places=2)

    history = HistoricalRecords()

    created_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Created Date'))

    modified_date = models.DateTimeField(default=timezone.now,
                                         verbose_name=_('Modified Date'))

    def __str__(self):
        return str(self.reference)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')



