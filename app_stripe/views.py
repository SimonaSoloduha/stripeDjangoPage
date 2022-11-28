from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app_stripe.models import Discount, TaxRate
from app_stripe.utils import create_discount_on_stripe, create_tax_rate_on_stripe


class DiscountListView(generic.ListView):
    model = Discount
    template_name = 'stripe/discount_list.html'
    context_object_name = 'discount_list'
    queryset = Discount.objects.all()


class DiscountCreateView(generic.CreateView):
    model = Discount
    fields = ['name', 'duration', 'percent_off']
    template_name = 'stripe/discount_create.html'
    success_url = reverse_lazy('discounts')

    def form_valid(self, form):
        with transaction.atomic():
            result = super(DiscountCreateView, self).form_valid(form)
            create_discount_on_stripe(self.object)
            return result


class DiscountDetailView(generic.DetailView):

    def get(self, request, discount_id):
        discount = Discount.objects.get(id=discount_id)
        return render(
            request,
            'stripe/discount_detail.html',
            context={
                'discount': discount,
            }
        )


class TaxRateListView(generic.ListView):
    model = TaxRate
    template_name = 'stripe/tax_rate_list.html'
    context_object_name = 'tax_rate_list'
    queryset = TaxRate.objects.all()


class TaxRateCreateView(generic.CreateView):
    model = TaxRate
    fields = ['display_name', 'inclusive', 'percentage']
    template_name = 'stripe/tax_rate_create.html'
    success_url = reverse_lazy('tax_rates')

    def form_valid(self, form):
        with transaction.atomic():
            result = super(TaxRateCreateView, self).form_valid(form)
            create_tax_rate_on_stripe(self.object)
            return result


class TaxRateDetailView(generic.DetailView):

    def get(self, request, tax_rate_id):
        tax_rate = TaxRate.objects.get(id=tax_rate_id)
        return render(
            request,
            'stripe/tax_rate_detail.html',
            context={
                'tax_rate': tax_rate,
            }
        )
