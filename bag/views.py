from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from artworks.models import Artwork, ArtFrame


def add_to_bag(request, artwork_id):
    """ Add a quantity of a specified artwork and
        its frame to the shopping bag
    """
    redirect_url = request.POST.get('redirect_url')
    frame_id = request.POST.get('frame')
    if not frame_id:
        messages.warning(request,
                         'Please select a Frame before adding to bag')
        return redirect(redirect_url)

    frame_id = int(frame_id)
    artwork = get_object_or_404(Artwork, pk=artwork_id)
    frame = get_object_or_404(ArtFrame, pk=frame_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity <= frame.qty:
        frame.qty -= quantity
        frame.save()
        # bag[frame_id] += quantity
        if artwork_id in list(bag.keys()):
            bag[artwork_id]['frame_id'][frame_id] += quantity
            messages.success(request,
                             f'Added {quantity} more {artwork.name} with frame \
                                {frame.name} to your bag',
                             extra_tags='bag_item_changed')
        else:
            bag[artwork_id] = {'frame_id': {frame_id: quantity}}
            messages.success(request,
                             f'{quantity} {artwork.name}  with frame \
                              {frame.name} added to your bag',
                             extra_tags='bag_item_changed')
    else:
        messages.error(request,
                       f'The quantity selected for {frame.name} \
                       is not available {frame.qty} in stock')
        return redirect(redirect_url)

    request.session['bag'] = bag
    return redirect(redirect_url)
