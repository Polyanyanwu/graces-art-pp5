from datetime import datetime
from django.db.models import Q
from .models import Order


def query_order(request, calling_module, order_status=None):
    """ Query the order table based on criteria entered by user
        If request type is post write the criteria to session
        If type is get, retrieve criteria from session
    Parameters:
        request : the request to extract the criteria from
        req_ty: a String of the request type
        calling_module: the function that called
        order_status: some modules have fixed order status
    Returns:
        filtered order table
    """
    if request.method == 'GET':
        query_dict = request.session.get(calling_module)
        if query_dict:
            sdate = query_dict['start_date']
            edate = query_dict['end_date']
            order_status = query_dict['order_status']
            order_number = query_dict['order_number']
            start_date = datetime.strptime(
                sdate, "%Y-%m-%d").date() if sdate else None
            end_date = datetime.strptime(
                edate, "%Y-%m-%d").date() if edate else None
            art_or_frame_name = query_dict['art_or_frame_name']
            email = query_dict['email']
        else:
            if order_status:
                return Order.objects.filter(
                    status=order_status).order_by('-date')
            else:
                return Order.objects.all().order_by('-date')
    else:
        order_status = request.POST.get('order_status') if request.POST.get(
            'order_status') else None

        sdate = request.POST.get('start_date') if request.POST.get(
            'start_date') else None
        start_date = datetime.strptime(
            sdate, "%Y-%m-%d").date() if sdate else None

        edate = request.POST.get('end_date') if request.POST.get(
            'end_date') else None
        end_date = datetime.strptime(
            edate, "%Y-%m-%d").date() if edate else None

        order_number = request.POST.get('order_number') if request.POST.get(
            'order_number') else None
        art_or_frame_name = request.POST.get(
                            'art_or_frame_name') if request.POST.get(
            'art_or_frame_name') else None
        email = request.POST.get('email') if request.POST.get(
            'email') else None
        query_dict = {}
        query_dict['start_date'] = sdate
        query_dict['end_date'] = edate
        query_dict['order_status'] = order_status
        query_dict['order_number'] = order_number
        query_dict['art_or_frame_name'] = art_or_frame_name
        query_dict['email'] = email
        request.session[calling_module] = query_dict

    if order_number:
        order = Order.objects.filter(order_number=order_number)
        if order.count() > 0:
            return order

    order = Order.objects.all().order_by('-date')
    if start_date and end_date:
        order = order.filter(
            Q(date__date__gte=start_date) &
            Q(date__date__lte=end_date))
    elif start_date:
        order = order.filter(date__date=start_date).order_by(
            '-date')
    elif end_date:
        order = order.filter(date__date=end_date).order_by(
            '-date')
    if order_status:
        order = order.filter(status=order_status)

    if email:
        order = order.filter(email=email)

    if art_or_frame_name:
        order = order.filter(
            (Q(line_items__artwork__name__icontains=art_or_frame_name)
                | Q(line_items__frame__name__icontains=art_or_frame_name))
                ).order_by('-date')
    return order
