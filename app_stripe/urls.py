from django.urls import path

from app_stripe.views import DiscountListView, DiscountCreateView, DiscountDetailView, \
    TaxRateListView, TaxRateCreateView, TaxRateDetailView

urlpatterns = [
    path('discounts/', DiscountListView.as_view(), name='discounts'),
    path('discounts/<int:discount_id>/', DiscountDetailView.as_view(), name='discount_detail'),
    path('discounts/create/', DiscountCreateView.as_view(), name='discount_create'),
    path('tax_rates/', TaxRateListView.as_view(), name='tax_rates'),
    path('tax_rates/<int:tax_rate_id>/', TaxRateDetailView.as_view(), name='tax_rate_detail'),
    path('tax_rates/create/', TaxRateCreateView.as_view(), name='tax_rate_create'),
]
