from django.db.models import Sum
from rest_framework import serializers

from app_items.models import Item, Order
from app_items.utils import create_checkout_session


class ItemSerializer(serializers.ModelSerializer):
    session_id = serializers.SerializerMethodField()

    def get_session_id(self, foo):
        session = create_checkout_session(name=foo.name, price=foo.price_usd, currency='usd',
                                          discount_id=None)
        return session.id

    class Meta:
        model = Item
        fields = ['session_id']


class OrderSerializer(serializers.ModelSerializer):
    session_id = serializers.SerializerMethodField()

    def get_session_id(self, foo):
        order = Order.objects.only('id', 'items__price_usd', 'items__price_rub').all(). \
            annotate(sum_order_usd=Sum('items__price_usd')).annotate(sum_order_rub=Sum('items__price_rub')). \
            get(id=foo.id)
        price = order.sum_order_usd
        session = create_checkout_session(name=f'ORDER number {foo.id}', price=price,
                                          currency='usd', discount_id=None)
        return session.id

    class Meta:
        model = Order
        fields = ['session_id']
