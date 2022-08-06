""" Home page views """
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from utility.models import SystemPreference
# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

@login_required
def coupons(request):
    """ A view to return the coupon toast
            ('CF', 'Customer welcome Coupon Code'),
            ('CR', 'Customer Threshold Coupon Code'),
            ('C1', 'Welcome coupon percentage discount'),
            ('T1', 'Threshold Amount'),
            ('C2', 'Threshold discount percentage')
    """
    welcome_code = get_object_or_404(SystemPreference, code='CF').data
    welcome_code_discount = get_object_or_404(SystemPreference, code='C1').data
    threshold_code = get_object_or_404(SystemPreference, code='CR').data
    threshold_amt = get_object_or_404(SystemPreference, code='T1').data
    threshold_discount = get_object_or_404(SystemPreference, code='C2').data

    return render(request, 'home/coupons.html',
                  {
                    'welcome_code': welcome_code,
                    'welcome_code_discount': welcome_code_discount,
                    'threshold_code': threshold_code,
                    'threshold_amt': threshold_amt,
                    'threshold_discount': threshold_discount,
                  })
