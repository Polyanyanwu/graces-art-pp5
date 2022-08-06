""" Model for Contact  Us message """

from django.db import models
from django.contrib.auth.models import User


class ContactUs(models.Model):
    """ Data model for contact us """

    options = [
            ('Information', 'Information'),
            ('My Order', 'My Order'),
            ('New Frame Request', 'New Frame Request'),
            ('Others', 'Others'),
        ]

    subject = models.CharField(choices=options, default='Information',
                               max_length=200, null=False, blank=False)
    message_body = models.TextField(null=False, blank=False)
    sender = models.EmailField(max_length=200, null=False, blank=False)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return str(self.sender)
