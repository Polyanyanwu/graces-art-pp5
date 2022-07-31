""" Views for Artworks and related tables update """

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from profiles.user_belong import check_in_group
from .forms import ArtistForm, ArtStyleForm, ArtGenreForm, ArtworkForm
from .models import Artist, ArtStyle, ArtGenre, Artwork


@login_required
@transaction.atomic
def maintain_artist(request):
    """ Maintain Artist """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    artists = Artist.objects.all().order_by('friendly_name')
    use_instance = True
    if artists.count() == 0:
        use_instance = False
        form = ArtistForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            name_sent = request.POST.get('name_selected')
            artist = get_object_or_404(Artist, name=name_sent)
            form = ArtistForm(instance=artist)
        elif 'create_new_record' in request.POST:
            form = ArtistForm()
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = ArtistForm(instance=artists[0])
            HttpResponseRedirect('artworks/artist.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            name_sent = request.POST.get('confirm-id')
            artist = get_object_or_404(Artist, name=name_sent)
            artist.delete()
            messages.success(request,
                             ('Artist ' + name_sent +
                              ' was successfully deleted!'))
            if use_instance:
                form = ArtistForm(instance=artists[0])
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
        if use_instance:
            form = ArtistForm(instance=artists[0])
    paginator = Paginator(artists, 10)  # Show 15 bookings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/artist.html', {
        'form': form,
        'artists': page_obj,
    })


@login_required
@transaction.atomic
def maintain_art_style(request):
    """ Maintain Art Styles """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    art_styles = ArtStyle.objects.all().order_by('friendly_name')
    use_instance = True
    if art_styles.count() == 0:
        use_instance = False
        form = ArtStyleForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            name_sent = request.POST.get('name_selected')
            art_style = get_object_or_404(ArtStyle, name=name_sent)
            form = ArtStyleForm(instance=art_style)
        elif 'create_new_record' in request.POST:
            form = ArtStyleForm()
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = ArtStyleForm(instance=art_styles[0])
            HttpResponseRedirect('artworks/art_style.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            name_sent = request.POST.get('confirm-id')
            art_genre = get_object_or_404(ArtStyle, name=name_sent)
            art_genre.delete()
            messages.success(request,
                             ('Art Style ' + name_sent +
                              ' was successfully deleted!'))
            if use_instance:
                form = ArtStyleForm(instance=art_styles[0])
        elif 'save_record' in request.POST:
            form = ArtStyleForm(data=request.POST)
            if form.is_valid():
                try:
                    art_style = ArtStyle.objects.get(
                                name=request.POST.get('name'))
                    art_style.name = request.POST.get('name')
                    art_style.friendly_name = request.POST.get('friendly_name')
                    art_style.save()
                except ObjectDoesNotExist:
                    form.save()
                messages.success(request,
                                 ('Your Art Style was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if use_instance:
            form = ArtStyleForm(instance=art_styles[0])
    paginator = Paginator(art_styles, 10)  # Show 15 bookings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/art_style.html', {
        'form': form,
        'art_styles': page_obj,
    })


@login_required
@transaction.atomic
def maintain_art_genre(request):
    """ Maintain Art Genre """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    art_genres = ArtGenre.objects.all().order_by('friendly_name')
    use_instance = True
    if art_genres.count() == 0:
        use_instance = False
        form = ArtGenreForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            name_sent = request.POST.get('name_selected')
            art_genre = get_object_or_404(ArtGenre, name=name_sent)
            form = ArtGenreForm(instance=art_genre)
        elif 'create_new_record' in request.POST:
            form = ArtGenreForm()
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = ArtGenreForm(instance=art_genres[0])
            HttpResponseRedirect('artworks/art_genre.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            name_sent = request.POST.get('confirm-id')
            art_genre = get_object_or_404(ArtGenre, name=name_sent)
            art_genre.delete()
            messages.success(request,
                             ('Art Genre ' + name_sent +
                              ' was successfully deleted!'))
            if use_instance:
                form = ArtGenreForm(instance=art_genres[0])
        elif 'save_record' in request.POST:
            form = ArtGenreForm(data=request.POST)
            if form.is_valid():
                try:
                    art_genre = ArtGenre.objects.get(
                                name=request.POST.get('name'))
                    art_genre.name = request.POST.get('name')
                    art_genre.friendly_name = request.POST.get('friendly_name')
                    art_genre.save()
                except ObjectDoesNotExist:
                    form.save()
                messages.success(request,
                                 ('Your Art Genre was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if use_instance:
            form = ArtGenreForm(instance=art_genres[0])
    paginator = Paginator(art_genres, 10)  # Show 15 bookings per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/art_genre.html', {
        'form': form,
        'art_genres': page_obj,
    })


def get_artworks(request):
    """ A view to display all Artworks """

    artworks = Artwork.objects.all()

    context = {
        'artworks': artworks,
    }

    return render(request, 'artworks/artworks.html', context)


@login_required
def add_artwork(request):
    """ Add artwork to the database """

    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an Artwork!')
        else:
            messages.error(request, 'Failed to add Artwork.\
                 Please check your input.')
    else:
        form = ArtworkForm()

    return render(request, 'artworks/add_artwork.html', {
        'form': form,
    })
