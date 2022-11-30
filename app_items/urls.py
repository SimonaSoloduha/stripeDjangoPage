from django.urls import path

from app_items.views import ItemListView, ItemCreateView, ItemDetailView, OrderListView, OrderCreateView, \
    OrderDetailView, ItemDetail

urlpatterns = [
    path('', ItemListView.as_view(), name='items'),
    path('<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('bay/<int:pk>/', ItemDetail.as_view(), name='items_detail_api'),
    path('bay_order/<int:pk>/', ItemDetail.as_view(), name='order_detail_api'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
]
