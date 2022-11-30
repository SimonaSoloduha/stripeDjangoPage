from django.db.models import Sum
from rest_framework import serializers

from app_items.models import Item, Order
from app_items.utils import create_checkout_session


class ItemSerializer(serializers.ModelSerializer):
    session_id = serializers.SerializerMethodField()

    def get_session_id(self, foo):
        discount_id = self.context["discount_id"]
        currency = self.context["currency"]
        if currency == 'usd' or currency is None:
            price = foo.price_usd
        else:
            price = foo.price_rub
            currency = 'rub'
        session = create_checkout_session(name=foo.name, price=price, currency=currency,
                                          discount_id=discount_id)
        return session.id

    class Meta:
        model = Item
        fields = ['session_id']


class OrderSerializer(serializers.ModelSerializer):
    session_id = serializers.SerializerMethodField()

    def get_session_id(self, foo):
        discount_id = self.context["discount_id"]
        currency = self.context["currency"]
        order = Order.objects.only('id', 'items__price_usd', 'items__price_rub').all(). \
            annotate(sum_order_usd=Sum('items__price_usd')).annotate(sum_order_rub=Sum('items__price_rub')). \
            get(id=foo.id)

        if currency == 'usd' or currency is None:
            price = order.sum_order_usd
        else:
            price = order.sum_order_rub
            currency = 'rub'
        session = create_checkout_session(name=f'ORDER number {foo.id}', price=price,
                                          currency=currency, discount_id=discount_id)
        return session.id

    class Meta:
        model = Order
        fields = ['session_id']
