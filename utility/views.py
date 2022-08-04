""" Utility Tables Maintenance View """

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.db.utils import DataError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .forms import SystemPreferenceForm, HomeMessageForm
from .models import SystemPreference, HomeMessage


class SystemPreferenceView(View):
    """ Maintain system preference records,
        requires administrator group membership"""

    def get(self, request, *args, **kwargs):
        """Display all system preference records and an update form"""

        syspref = SystemPreference.objects.all()
        selected_item = syspref[0].code
        form = SystemPreferenceForm(instance=syspref[0])
        return render(
            request,
            "utility/sys_pref/sys_pref.html",
            {
                "form": form,
                "syspref": syspref,
                "pref_code": selected_item
            }
        )

    def post(self, request, *args, **kwargs):
        """ Update selected system preference record """

        if 'save_system_preference' in request.POST:  # save button clicked
            selected_item = request.POST.get('pref_code')
            pref_form = get_object_or_404(SystemPreference, code=selected_item)
            data = int(request.POST.get('data'))
            pref_form.data = data
            try:
                pref_form.save()
                messages.add_message(request, messages.INFO,
                                     'Data updated successfully')
            except DataError:
                print(" Data error saving system preference ")
                messages.add_message(request, messages.INFO,
                                     'Error saving cancellation, try later')
            syspref = SystemPreference.objects.all()
            form = SystemPreferenceForm(instance=syspref[0])
            selected_item = syspref[0].code
        else:
            selected_item = request.POST.get('pref_code')
            syspref = SystemPreference.objects.all()
            curr = None
            try:
                curr = SystemPreference.objects.get(code=selected_item)
            except ObjectDoesNotExist as exception:
                print(exception)
            if curr:
                form = SystemPreferenceForm(instance=curr)
            else:
                form = SystemPreferenceForm(instance=syspref[0])

        return render(
            request,
            "utility/sys_pref/sys_pref.html",
            {
                "form": form,
                "syspref": syspref,
                "pref_code": selected_item
            }
        )


class HomeMessageView(View):
    """ Maintain general information,
        requires administrator group membership"""

    def get(self, request, *args, **kwargs):
        """Display all general information records and an update form"""

        info = HomeMessage.objects.all()
        selected_item = info[0].code
        form = HomeMessageForm(instance=info[0])
        return render(
            request,
            "utility/info/general_info.html",
            {
                "form": form,
                "info": info,
                "info_code": selected_item
            }
        )

    def post(self, request, *args, **kwargs):
        """ Update selected record """
        if 'save_gen_info' in request.POST:  # save button clicked

            selected_item = request.POST.get('code')
            info_form = get_object_or_404(HomeMessage, code=selected_item)
            data = request.POST.get('description')
            info_form.description = data
            try:
                info_form.save()
                messages.add_message(request, messages.INFO,
                                     'Data updated successfully')
            except DataError:
                print(" Data error saving system preference ")
                messages.add_message(request, messages.INFO,
                                     'Error saving cancellation, try later')
            # info = HomeMessage.objects.all()
            form = HomeMessageForm(instance=info_form)
            info = info_form
        else:
            selected_item = request.POST.get('info_code')
            info = HomeMessage.objects.all()
            curr = None
            try:
                curr = HomeMessage.objects.get(code=selected_item)
            except ObjectDoesNotExist as exception:
                print(exception)
            if curr:
                form = HomeMessageForm(instance=curr)
            else:
                form = HomeMessageForm(instance=info[0])

        return render(
            request,
            "utility/info/general_info.html",
            {
                "form": form,
                "info": info,
                "info_code": selected_item
            }
        )


def terms_of_use(request):
    """ View terms of use message """
    info = get_object_or_404(HomeMessage, code='T')
    return render(
          request,
          "utility/terms_of_use.html",
          {
              "info": info,
          }
      )
