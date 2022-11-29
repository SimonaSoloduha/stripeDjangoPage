from django.db import models
from django.utils.translation import gettext_lazy as _

DURATION_CHOICES = [
    ('once', 'Once'),
    ('forever', 'Forever'),
    ('repeating', 'Repeating'),
]


class Discount(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    duration = models.CharField(
        max_length=10,
        choices=DURATION_CHOICES,
        default='forever',
        verbose_name=_('duration')
    )
    percent_off = models.DecimalField(max_digits=100, decimal_places=1, default=10, verbose_name=_('percent off'))
    stripe_id = models.CharField(max_length=100, blank=True, verbose_name=_('stripe_id'))

    class Meta:
        verbose_name = _('discount')
        verbose_name_plural = _('discounts')

    def __str__(self):
        return f'{self.name}'


class TaxRate(models.Model):
    display_name = models.CharField(max_length=100, verbose_name=_('display name'))
    inclusive = models.BooleanField(default=False, verbose_name=_('inclusive'))
    percentage = models.DecimalField(max_digits=100, decimal_places=1, default=10, verbose_name=_('percentage'))
    stripe_id = models.CharField(max_length=100, blank=True, verbose_name=_('id_in_stripe'))

    class Meta:
        verbose_name = _('tax rate')
        verbose_name_plural = _('tax rates')

    def __str__(self):
        return f'{self.display_name}'
