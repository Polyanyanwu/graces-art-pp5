""" Views for Artworks and related tables update """

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from profiles.user_belong import check_in_group
from .forms import ArtistForm, ArtStyleForm, ArtGenreForm, ArtworkForm, ArtFrameForm
from .models import Artist, ArtStyle, ArtGenre, Artwork, ArtFrame


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
    direction = None
    if request.GET:
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            artworks = artworks.order_by(sort_key)
        if 'artist' in request.GET:
            artworks = artworks.filter(artist__name=request.GET['artist'])
        if 'genre' in request.GET:
            artworks = artworks.filter(genre__name=request.GET['genre'])
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


def edit_delete_artwork(request):
    """ Edit/Delete Artwork """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')
    artworks = Artwork.objects.all().order_by('artist')
    recs_available = artworks.count() > 0

    # artwork = None
    # form = None
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            id_sent = request.POST.get('name_selected')
            artwork = get_object_or_404(Artwork, pk=int(id_sent))
            form = ArtworkForm(instance=artwork)
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            artwork = get_object_or_404(Artwork, pk=int(id_sent))
            name = artwork.name
            artwork.delete()
            messages.success(request,
                             ('Artwork ' + name +
                              ' was successfully deleted!'))
            artworks = Artwork.objects.all().order_by('artist')
            if artworks.count() > 0:
                form = ArtworkForm(instance=artworks[0])
                HttpResponseRedirect('artworks/edit_delete_artwork.html')
        elif 'cancel_ops' in request.POST:
            if recs_available:
                form = ArtworkForm(instance=artworks[0])
            HttpResponseRedirect('artworks/edit_delete_artwork.html')
        elif 'save_record' in request.POST:
            artwork = get_object_or_404(Artwork, sku=request.POST.get('sku'))
            form = ArtworkForm(request.POST, request.FILES, instance=artwork)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 ('Your Artwork was successfully updated!'))
            else:
                messages.error(request, ('Please correct the error below.'))
        elif 'run-query' in request.POST:
            sku = request.POST.get('q_sku')
            if sku:
                artworks = Artwork.objects.filter(sku=sku)
                if artworks.count() > 0:
                    form = ArtworkForm(instance=artworks[0])
                else:
                    artworks = Artwork.objects.all().order_by('artist')
                    if artworks.count() > 0:
                        form = ArtworkForm(instance=artworks[0])
            else:
                name = request.POST.get('q_name')
                if name:
                    artworks = Artwork.objects.filter(name__icontains=name)
                    if artworks.count() > 0:
                        form = ArtworkForm(instance=artworks[0])
                    else:
                        artworks = Artwork.objects.all().order_by('artist')
                        if artworks.count() > 0:
                            form = ArtworkForm(instance=artworks[0])
    else:
        artworks = Artwork.objects.all().order_by('artist')
        recs_available = artworks.count() > 0
        if recs_available:
            form = ArtworkForm(instance=artworks[0])
    paginator = Paginator(artworks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/edit_delete_artwork.html', {
        'form': form,
        'artworks': page_obj,
    })


def edit_delete_artwork_single(request, artwork_id):
    """ Edit/Delete Artwork - single record """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    if request.method == 'POST':
        if 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            artwork = get_object_or_404(Artwork, pk=int(id_sent))
            name = artwork.name
            artwork.delete()
            messages.success(request, ('Artwork ' + name +
                             ' was successfully deleted!'))
            return redirect(reverse('get_artworks'))

        elif 'cancel_ops' in request.POST:
            return redirect(reverse('get_artworks'))
        elif 'save_record' in request.POST:
            artwork = get_object_or_404(Artwork, sku=request.POST.get('sku'))
            form = ArtworkForm(request.POST, request.FILES, instance=artwork)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 ('Your Artwork was successfully updated!'))
            else:
                messages.error(request, ('Please correct the error below.'))
            # redirect to product details later
    else:
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        form = ArtworkForm(instance=artwork)
    return render(request, 'artworks/edit_delete_single_artwork.html', {
        'form': form,
        'artwork': artwork,
    })


@login_required
@transaction.atomic
def maintain_art_frame(request):
    """ Maintain Art Frames """
    # check that user is administrator
    rights = check_in_group(request.user, ("administrator",))
    if rights != "OK":
        messages.error(request, (rights))
        return redirect('/')

    art_frames = ArtFrame.objects.all().order_by('size')
    use_instance = True
    if art_frames.count() == 0:
        use_instance = False
        form = ArtFrameForm()
    if request.method == 'POST':
        if 'select_rec' in request.POST:
            id_sent = request.POST.get('name_selected')
            request.session['current_rec'] = id_sent
            art_frame = get_object_or_404(ArtFrame, pk=int(id_sent))
            form = ArtFrameForm(instance=art_frame)
        elif 'create_new_record' in request.POST:
            request.session['current_rec'] = ""
            form = ArtFrameForm()
        elif 'cancel_ops' in request.POST:
            if use_instance:
                form = ArtFrameForm(instance=art_frames[0])
                request.session['current_rec'] = art_frames[0].id
            HttpResponseRedirect('artworks/art_frame.html')
        elif 'confirm-action-btn' in request.POST:
            # action is only delete action
            id_sent = request.POST.get('confirm-id')
            art_frame = get_object_or_404(ArtFrame, pk=int(id_sent))
            name = art_frame.name
            art_frame.delete()
            request.session['current_rec'] = ""
            messages.success(request,
                             ('Art frame ' + name +
                              ' was successfully deleted!'))
            art_frames = ArtFrame.objects.all().order_by('size')
            if art_frames.count() > 0:
                form = ArtFrameForm(instance=art_frames[0])
                request.session['current_rec'] = art_frames[0].id
        elif 'save_record' in request.POST:
            if request.session.get('current_rec'):
                frame_id = int(request.session.get('current_rec'))
                art_frame = get_object_or_404(ArtFrame,
                                              pk=frame_id)
                form = ArtFrameForm(request.POST, request.FILES,
                                    instance=art_frame)
            else:
                form = ArtFrameForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 ('Your Art Frame was successfully saved!'))
            else:
                messages.error(request, ('Please correct the error below.'))
    else:
        if use_instance:
            form = ArtFrameForm(instance=art_frames[0])
            request.session['current_rec'] = art_frames[0].id
    paginator = Paginator(art_frames, 10)  # Show 10 recs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artworks/art_frame.html', {
        'form': form,
        'art_frames': page_obj,
    })
