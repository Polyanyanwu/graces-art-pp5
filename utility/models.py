""" General tables used at some of the applications """

from django.db import models


class SystemPreference(models.Model):
    """ Variables for system to operate
        Maintained by the Administrator"""
    SYSTEM_OPTIONS = [
            ('S', 'Sales Percentage'),
            ('D', 'Description of Current Sales'),
            ('R', 'Return Valid Days'),
            ('C', 'Cancellation Valid Days'),
            ('Q', 'Maximum Customer Selectable Quantity'),
            ('CF', 'Customer welcome Coupon Code'),
            ('CR', 'Customer Threshold Coupon Code'),
            ('C1', 'Welcome coupon percentage discount'),
            ('T1', 'Threshold Amount'),
            ('C2', 'Threshold discount percentage'),
            ('DP', 'Delivery Charge Percentage'),
            ('DC', 'Delivery Cost Maximum'),

        ]
    DATA_TYPES = [
            ('str', 'Text'),
            ('int', 'Integer'),
        ]

    code = models.CharField(primary_key=True, choices=SYSTEM_OPTIONS,
                            default='S', max_length=2)
    data = models.CharField(max_length=50, blank=False)
    data_type = models.CharField(max_length=3, blank=False,
                                 choices=DATA_TYPES)
    # data types will be str or int used to validate input

    def __str__(self):
        return str(self.code)

    def get_preference_name(self):
        """ return the data """
        return self.data

    def pref_verbose(self):
        """ Method to return the verbose name of the option """
        return dict(SystemPreference.SYSTEM_OPTIONS)[self.code]


class HomeMessage(models.Model):
    """ Description of messages on home page
        plus Terms of Use, Privacy Policy, About Us
        To prevent hard-coding of information """
    CHOICES = [
        ('T', 'Terms of Use'),
        ('P', 'Privacy Policy'),
        ('A', 'About Us'),
        ('H', 'Home Welcome Message'),
    ]

    code = models.CharField(max_length=1, primary_key=True, choices=CHOICES)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.description)

    def verbose_name(self):
        """ Method to return the verbose name of the option """
        return dict(HomeMessage.CHOICES)[self.code]
