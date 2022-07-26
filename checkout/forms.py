""" Order form for Checkout
"""


from django import forms
from .models import Order, ReturnOrder, CancelOrder


class OrderForm(forms.ModelForm):
    """ Order form setting
        Adopted from Code Institute Boutique walk through project
    """
    class Meta:
        """ Order Form meta """
        model = Order
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'street_address1', 'street_address2', 'postal_code',
                  'town_city', 'county_region', 'country', 'discount_code')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'postal_code': 'Postal Code',
            'town_city': 'Town or City',
            'county_region': 'County or Region',
            'discount_code': 'Discount Code',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class ReturnOrderForm(forms.ModelForm):
    """ Return Order model form """
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}))

    class Meta:
        """ Return Order Form meta """
        model = ReturnOrder
        fields = ('reason',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs['placeholder'] = 'Enter your reason'


class CancelOrderForm(forms.ModelForm):
    """ Cancel Order model form """
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}))

    class Meta:
        """ Cancel Order Form meta """
        model = CancelOrder
        fields = ('reason',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        place_h = 'Do let us know why to enable us serve you better in future'
        self.fields['reason'].widget.attrs['placeholder'] = place_h
