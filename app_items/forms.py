from django import forms

from app_items.models import Order, Item

CURRENCY_CHOICES = (
    ("usd", "USD"),
    ("rub", "RUB"),
)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['items', 'discount', 'tax_rate']

    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class ChangeCurrency(forms.Form):
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)
