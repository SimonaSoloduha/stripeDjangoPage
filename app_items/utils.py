import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_API_KEY


def create_checkout_session(name, price, discount_id, currency):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': currency,
                'product_data': {
                    'name': name,
                },
                'unit_amount': price * 100,
                "tax_behavior": "exclusive",
            },
            "adjustable_quantity": {"enabled": True, "minimum": 1, "maximum": 10},
            "quantity": 1,
        }],
        automatic_tax={"enabled": True},
        mode='payment',
        discounts=[{
            'coupon': discount_id,
        }],
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    return session


def create_item_on_stripe(obj):
    product = stripe.Product.create(name=obj.name, tax_code='txcd_10000000')
    price = stripe.Price.create(
        unit_amount=obj.price_usd,
        currency='USD',
        recurring={"interval": "month"},
        product=product.id,
        tax_behavior="exclusive",
    )
    obj.stripe_id = product.id
    obj.stripe_price = price.id
    obj.save(update_fields=['stripe_id', 'stripe_price'])
