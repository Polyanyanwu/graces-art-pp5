from django.shortcuts import render, redirect, get_object_or_404
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

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    frame = get_object_or_404(ArtFrame, pk=int(frame_id))
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity <= frame.qty:
        frame.qty -= quantity
        frame.save()
        id_string = str(artwork_id) + "-" + frame_id

        if id_string in list(bag.keys()):
            frame_key = list(bag[id_string]['frame_id'].keys())[0]
            if frame_id == frame_key:
                # same artwork and frame
                bag[id_string]['frame_id'][frame_key] += quantity
            else:
                # new frame with same artwork
                bag[str(artwork_id) + "-" + frame_id] = \
                    {'frame_id': {frame_id: quantity}}

            messages.success(request,
                             f'Added {quantity} more {artwork.name} with frame \
                                {frame.name} to your bag',
                             extra_tags='bag_item_changed')
        else:
            print(type(artwork_id), type(frame_id))
            bag[str(artwork_id) + "-" + frame_id] = \
                {'frame_id': {frame_id: quantity}}
            messages.success(request,
                             f'{quantity} {artwork.name}  with frame \
                              {frame.name} added to your bag',
                             extra_tags='bag_item_changed')
    else:
        messages.warning(request,
                         f'The quantity selected for {frame.name} \
                         is not available {frame.qty} in stock')
        return redirect(redirect_url)
    request.session['bag'] = bag
    return redirect(redirect_url)


def view_bag(request):
    """ A view that renders the bag contents page
        Data is in the context already """

    return render(request, 'bag/bag.html')
