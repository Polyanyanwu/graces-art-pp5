from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from artworks.models import Artwork, ArtFrame


def add_to_bag(request, item_id):
    """ Add a quantity of a specified artwork and
        its frame to the shopping bag
    """
    frame_id = int(request.POST.get('frame'))
    artwork = get_object_or_404(Artwork, pk=item_id)
    frame = get_object_or_404(ArtFrame, pk=frame_id)
    quantity = int(request.POST.get('quantity'))

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if quantity <= frame.qty:
        if frame_id in list(bag.keys()):
            bag[frame_id] += quantity
            frame.qty -= quantity
            frame.save()
            messages.success(request,
                             f'Added {quantity} more {artwork.name} with frame \
                                {frame.name} to your bag')
        else:
            bag[frame_id] = quantity
            frame.qty -= quantity
            frame.save()
            messages.success(request,
                             f'{quantity} {artwork.name}  with frame \
                              {frame.name} added to your bag')
    else:
        messages.error(request,
                       f'The quantity selected for {frame.name} \
                       is not available {frame.qty} in stock')
        return redirect(redirect_url)

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)
