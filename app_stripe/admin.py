from django.contrib import admin
from app_stripe.models import Discount, TaxRate


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TaxRateAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name')


admin.site.register(Discount, DiscountAdmin)
admin.site.register(TaxRate, TaxRateAdmin)
