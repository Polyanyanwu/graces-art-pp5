""" Forms for the User profile app """

from django import forms
from .models import UserProfile, UserGroup


class UserProfileForm(forms.ModelForm):
    """ User profile form """
    field_order = ['first_name', 'last_name', 'phone', 'postal_code',
                   'town_city', 'street_address1', 'street_address2',
                   'county_region', 'country']

    class Meta:
        """ Meta for User Profile """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'Firstname',
            'last_name': 'Lastname',
            'phone': 'Phone Number',
            'postal_code': 'Postal Code',
            'town_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county_region': 'County, State or Locality',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False

    def save(self, request):
        """ Update the User table with the new first and last name """
        user = super(UserProfileForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class GroupForm(forms.ModelForm):
    """ Enable select user group """
    class Meta:
        """ Specify the profile fields to update """
        model = UserGroup
        fields = ('user', 'group_name')
