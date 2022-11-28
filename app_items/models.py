from django.db import models
from django.utils.translation import gettext_lazy as _

from app_stripe.models import Discount, TaxRate


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    price_usd = models.PositiveIntegerField(verbose_name=_('price usd'))
    price_rub = models.PositiveIntegerField(verbose_name=_('price rub'))
    stripe_price = models.CharField(max_length=100, blank=True, default='', verbose_name=_('price_stripe'))
    stripe_id = models.CharField(max_length=100, blank=True, default='', verbose_name=_('stripe_id'))
    description = models.TextField(verbose_name=_('description'), blank=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, null=True, verbose_name=_('items'), related_name='order')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    payment_at = models.DateTimeField(null=True, verbose_name=_('payment_at'))
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, verbose_name=_('discount'),
                                 related_name='order')
    tax_rate = models.ForeignKey(TaxRate, on_delete=models.SET_NULL, null=True, verbose_name=_('tax rate'),
                                 related_name='order')

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return f'order of {self.created_at}'
