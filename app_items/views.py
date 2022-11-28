from django.db import transaction
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from app_items.forms import OrderCreateForm, ChangeCurrency

from app_items.models import Item, Order
from app_items.utils import create_item_on_stripe, create_checkout_session


class ItemListView(generic.ListView):
    model = Item
    template_name = 'item/item_list.html'
    context_object_name = 'item_list'
    queryset = Item.objects.all()


class ItemCreateView(generic.CreateView):
    model = Item
    fields = ['name', 'price_usd', 'price_rub', 'description']
    template_name = 'item/item_create.html'
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        with transaction.atomic():
            result = super(ItemCreateView, self).form_valid(form)
            create_item_on_stripe(self.object)
            return result


class ItemDetailView(generic.DetailView):

    def get(self, request, item_id):
        item = Item.objects.get(id=item_id)
        print('PRICEEE!', item.stripe_price)

        form = ChangeCurrency()
        return render(
            request,
            'item/item_detail.html',
            context={
                'item': item,
                'form': form,
            }
        )

    def post(self, request, item_id):
        item = Item.objects.get(id=item_id)
        form = ChangeCurrency(request.POST)
        if form.is_valid():
            currency = form.cleaned_data["currency"]
            if currency == 'USD':
                price = item.price_usd
            else:
                price = item.price_rub
            discount_id = None
            session = create_checkout_session(name=item.name, price=price, currency=currency,
                                              discount_id=discount_id)
            return redirect(session.url)


class OrderListView(generic.ListView):
    model = Order
    template_name = 'item/order_list.html'
    context_object_name = 'order_list'
    queryset = Order.objects.only('id', 'items__price_usd').all().annotate(sum_order=Sum('items__price_usd')).all()


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'item/order_create.html'
    success_url = reverse_lazy('orders')


class OrderDetailView(generic.DetailView):

    def get(self, request, order_id):
        form = ChangeCurrency()
        order = Order.objects.only('id', 'items__price_usd', 'items__price_rub', 'discount', 'tax_rate').all().\
            annotate(sum_order_usd=Sum('items__price_usd')).annotate(sum_order_rub=Sum('items__price_rub')).\
            get(id=order_id)
        return render(
            request,
            'item/order_detail.html',
            context={
                'order': order,
                'form': form,
            }
        )

    def post(self, request, order_id):
        order = Order.objects.only('id', 'items__price_usd', 'items__price_rub').all().\
            annotate(sum_order_usd=Sum('items__price_usd')).annotate(sum_order_rub=Sum('items__price_rub')).\
            get(id=order_id)
        form = ChangeCurrency(request.POST)
        if form.is_valid():
            currency = form.cleaned_data["currency"]
            if currency == 'USD':
                price = order.sum_order_usd
            else:
                price = order.sum_order_rub
            if order.discount:
                discount_id = order.discount.id
            else:
                discount_id = None
            session = create_checkout_session(name=f'ORDER number {order.id}', price=price,
                                              currency=currency, discount_id=discount_id)
            return redirect(session.url)
