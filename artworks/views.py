""" Views for Artworks and related tables update """

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
# from profiles.user_belong import check_in_group
from .forms import ArtistForm
from .models import Artist


@login_required
@transaction.atomic
def maintain_artist(request):
    """ Maintain Artist """
    artists = Artist.objects.all().order_by('friendly_name')
    if request.method == 'POST':
        print(request.POST)
        if 'select_rec' in request.POST:
            name_sent = request.POST.get('name_selected')
            artist = get_object_or_404(Artist, name=name_sent)
            form = ArtistForm(instance=artist)
        elif 'create_new_record' in request.POST:
            form = ArtistForm()
        elif 'cancel_ops' in request.POST:
            form = ArtistForm(instance=artists[0])
            HttpResponseRedirect('artworks/artist.html')
        elif 'save_record' in request.POST:
            form = ArtistForm(data=request.POST)
            if form.is_valid():
                try:
                    artist = Artist.objects.get(name=request.POST.get('name'))
                    artist.name = request.POST.get('name')
                    artist.friendly_name = request.POST.get('friendly_name')
                    artist.save()
                except ObjectDoesNotExist:
                    form.save()
                messages.success(request,
                                 ('Your Artist was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        form = ArtistForm(instance=artists[0])
    paginator = Paginator(artists, 10)  # Show 15 bookings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/artist.html', {
        'form': form,
        'artists': page_obj,
    })
