""" Model for Contact  Us message """

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from checkout.models import Notification
from profiles.models import UserProfile


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
        """ verbose name of the table """
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return str(self.sender)

    def send_contact_message(self):
        """
        Send confirmation email when a contact completes a contact form
        """

        sender = self.sender
        subject = 'Your message to us'
        body = render_to_string(
            'home/messages/contact_email.txt',
            {'details': self})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [sender]
        )

    # Write notification record
        if self.user:
            user = UserProfile.objects.get(user=self.user)
            Notification.objects.create(
                subject=subject + ": " + user.get_fullname(),
                message=body,
                user=user)


class Review(models.Model):
    """ Data model for User Reviews """

    RATINGS = [
            ('0', '0'),  # zeo will fail validation
            (1, 'One star'),
            (2, 'Two star'),
            (3, 'Three star'),
            (4, 'Four star'),
            (5, 'Five star'),
        ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL,
                             null=True, blank=True)
    rating = models.SmallIntegerField(choices=RATINGS, default='0',
                                      null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
