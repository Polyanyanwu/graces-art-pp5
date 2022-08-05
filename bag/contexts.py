""" Context processor for the shopping bag """

from decimal import Decimal
from django.shortcuts import get_object_or_404
from artworks.models import Artwork, ArtFrame
from utility.models import SystemPreference


def bag_contents(request):
    """
    Compute the content of the shopping bag include delivery cost
    and grand total
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    coupon_delta = 0

    for item_id, frame_detail in bag.items():
        artwork_id = item_id.split('-')[0]
        artwork = get_object_or_404(Artwork, pk=artwork_id)
        frame = get_object_or_404(ArtFrame,
                                  pk=list(frame_detail['frame_id'].keys())[0])

        quantity = list(frame_detail['frame_id'].values())[0]
        product_count += quantity
        if artwork.on_sale:
            sale_price = float(artwork.get_sale_price())
            product_subtotal = quantity * (Decimal(sale_price)
                                           + frame.price)
            price = sale_price
        else:
            product_subtotal = Decimal(quantity *
                                       (artwork.price + frame.price))
            price = artwork.price
        total += product_subtotal
        bag_items.append({
            'artwork_id': artwork_id,
            'quantity': quantity,
            'artwork': artwork,
            'frame': frame,
            'artwork_price': price,
            'sub_total': product_subtotal,
        })
    delivery_cost = Decimal(int(get_object_or_404(SystemPreference,
                            code='DP').data) * total / 100)
    max_delivery_cost = Decimal(get_object_or_404(SystemPreference,
                                code='DC').data)
    if delivery_cost > max_delivery_cost:
        delivery_cost = max_delivery_cost

    coupon_threshold = float(get_object_or_404(SystemPreference,
                             code='T1').data)
    if float(total) < coupon_threshold:
        coupon_delta = Decimal(coupon_threshold - float(total))

    grand_total = delivery_cost + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'coupon_delta': coupon_delta,
        'coupon_threshold': coupon_threshold,
        'grand_total': grand_total,
    }
    return context
