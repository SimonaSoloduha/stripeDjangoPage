from django.contrib import admin

from app_items.models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
