""" Module for User Profile """
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country', null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_city = models.CharField(max_length=40, null=True, blank=True)
    county_region = models.CharField(max_length=80, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    used_welcome_coupon = models.BooleanField(null=False,
                                              blank=False, default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class UserGroup(models.Model):
    """ Used to enable select group for updating user group """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group_name = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self):
        ''' String method to return the group '''
        return self.group_name.name
