""" Views for Profile and Group update """

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .forms import UserProfileForm
from .models import UserProfile


@login_required
@transaction.atomic
def update_profile(request):
    """ Update user profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save(request)
            messages.success(request,
                             ('Your profile was successfully updated!'))
            # return redirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'profiles/user_profile.html', {
        'profile_form': profile_form
    })
