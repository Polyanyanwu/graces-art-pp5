""" Module to display, update or delete bag items """

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from artworks.models import Artwork, ArtFrame
from utility.models import SystemPreference
from bag.models import WishList


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
    max_qty_rec = get_object_or_404(SystemPreference, code='Q')
    max_qty = int(max_qty_rec.data) + 1

    frames = ArtFrame.objects.all()

    return render(request, 'bag/bag.html',
                  {
                        'max_qty':  range(1, max_qty),
                        'frames': frames,
                  })


def update_bag(request):
    """ A view that updates/deletes bag contents
        Data is in the context already """

    bag = request.session.get('bag', {})
    if 'confirm-action-btn' in request.POST:
        # confirmation of remove action
        try:
            item_id = request.POST.get('confirm-id')
            artwork_id = item_id.split('-')[0]
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            bag.pop(item_id)
            messages.success(request, f'Removed {artwork.name} from your bag')
            request.session['bag'] = bag
        except Exception as e:
            messages.error(request, f'Error removing item: {e}')

    elif 'confirm-moveto-wishlist' in request.POST:
        # confirmation of move to wishlist action
        try:
            rec = request.POST.get('confirm-moveto-wishlist')
            item_id = rec.split(':')[0]
            qty = int(rec.split(':')[1])
            artwork_id = item_id.split('-')[0]
            frame_id = item_id.split('-')[1]
            artwork = get_object_or_404(Artwork, pk=artwork_id)
            frame = get_object_or_404(ArtFrame, pk=frame_id)
            frame.qty += qty
            frame.save()
            bag.pop(item_id)
            request.session['bag'] = bag
            add_to_wishlist(request, artwork_id)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')

    if 'change-qty-btn' in request.POST:
        # change of bag item quantity
        # need to confirm availability of the new frame quantity
        try:
            item_id = request.POST.get('change-qty-btn')
            frame_id = item_id.split('-')[1].split(':')[0]
            new_qty = int(item_id.split(':')[1])
            bag_item_key = item_id.split(':')[0]
            old_qty = bag[bag_item_key]['frame_id'][frame_id]

            frame = get_object_or_404(ArtFrame, pk=int(int(frame_id)))
            if new_qty > old_qty and (new_qty - old_qty) > frame.qty:
                messages.warning(request,
                                 f'The quantity selected for {frame.name} \
                                 is not available: Only {frame.qty} in stock')
                return redirect('view_bag')
            frame.qty -= (new_qty - old_qty)
            frame.save()
            bag[bag_item_key]['frame_id'][frame_id] = int(new_qty)
            messages.success(request, f'Updated quantity of {frame.name}\
                 in your bag')
        except Exception as e:
            messages.error(request, 'Error removing item: contact \
                site owner if it persists')
            print(f'Error removing item: {e}')

    if 'change-frame-btn' in request.POST:
        # change of frame type
        # need to confirm availability of the new frame quantity
        try:
            item_id = request.POST.get('change-frame-btn')
            old_frame = item_id.split('-')[1].split(':')[0]
            artwork_id = item_id.split('-')[0]
            new_frame = int(item_id.split(':')[1])
            bag_item_key = item_id.split(':')[0]
            frame_qty = bag[bag_item_key]['frame_id'][old_frame]

            frame = get_object_or_404(ArtFrame, pk=int(int(new_frame)))
            if frame_qty > frame.qty:
                messages.warning(request,
                                 f'The quantity selected for {frame.name} \
                                 is not available: Only {frame.qty} in stock')
                return redirect('view_bag')
            frame.qty -= frame_qty
            frame.save()
            # remove the item but increase the quantity
            # if the new frame exists with the same artwork id
            bag.pop(bag_item_key)
            new_frame = str(new_frame)
            new_bag_key = artwork_id + '-' + new_frame

            if new_bag_key in list(bag.keys()):
                bag[new_bag_key]['frame_id'][new_frame] += frame_qty
            else:
                bag[new_bag_key] = {'frame_id': {new_frame: frame_qty}}

            messages.success(request, f'Updated frame to {frame.name}\
                 in your bag')
        except Exception as e:
            messages.error(request, 'Error removing item: contact \
                site owner if it persists')
            print(f'Error removing item: {e}')
    return redirect('view_bag')


def add_to_wishlist(request, artwork_id):
    """ Add an artwork to wishlist """

    redirect_url = request.META.get('HTTP_REFERER')
    if not request.user.is_authenticated:
        messages.info(request, "You need to login before using this feature")
        return redirect(redirect_url)

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    existing = WishList.objects.filter(artwork=artwork)

    if existing.count() > 0:
        messages.info(request, f"{existing[0].artwork.name} \
            already in your wishlist")
        return redirect(redirect_url)
    try:
        WishList.objects.create(
            artwork=artwork,
            user=request.user)
        messages.success(request, f"{artwork.name} \
            has been added to your wishlist")
    except Exception as ex:
        print("Error adding wishlist", ex)
        messages.error(request, f"{artwork.name} could \
            not be added now. Try later or contact site owner")
    return redirect(redirect_url)
