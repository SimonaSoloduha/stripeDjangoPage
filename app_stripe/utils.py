from datetime import datetime

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_discount_on_stripe(obj):
    now = datetime.now()
    date_time = now.strftime("%m%d%Y%H%M%S")
    discount = stripe.Coupon.create(duration=obj.duration, id=f'{obj.id}_{date_time}', percent_off=obj.percent_off)
    obj.stripe_id = discount.id
    obj.save(update_fields=['stripe_id'])


def create_tax_rate_on_stripe(obj):
    tax = stripe.TaxRate.create(
      display_name=obj.display_name,
      percentage=obj.percentage,
      inclusive=obj.inclusive,
    )
    obj.stripe_id = tax.id
    obj.save(update_fields=['stripe_id'])
