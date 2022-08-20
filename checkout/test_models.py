""" Testing of Order Models """

from datetime import datetime
from django.test import TestCase
from artworks.models import Artwork, ArtFrame
from .models import Notification, Order, OrderLineItem


class TesItemForm(TestCase):
    """ Form testing class"""
    fixtures = ["test_fixture/artframe.json",
                "test_fixture/system_preference.json",
                "test_fixture/order_status.json",
                "test_fixture/artist.json",
                "test_fixture/artstyle.json",
                "test_fixture/artgenre.json",
                "test_fixture/artwork.json"]

    def test_notification_user_is_required(self):
        """ test notification user is required """
        with self.assertRaisesMessage(ValueError, 'Cannot assign'):
            Notification.objects.create(subject='Test Subject',
                                        message='Test message',
                                        notice_date=datetime.now(), user="")

    def test_order_number_is_generated(self):
        """ Test that Order Number is created
        """
        Order.objects.create(
            order_total=0,
        )
        # Check that order record is created
        self.assertTrue(len(list(Order.objects.all())) > 0)
        order = Order.objects.get(id=1)
        order_id = order.order_number
        # Check Order Number is generated
        self.assertIsNotNone(order_id)

    def test_update_of_order_table(self):
        """ Test that adding line items updates the order table """
        Order.objects.create(
            order_total=0,
        )
        order = Order.objects.get(id=1)
        artwork = Artwork.objects.get(pk=1)
        frame = ArtFrame.objects.get(pk=1)

        OrderLineItem.objects.create(
            order=order,
            artwork=artwork,
            frame=frame,
            quantity=1,
            artwork_price=artwork.price,
            frame_price=frame.price,
        )
        line_item = OrderLineItem.objects.get(id=1)
        # assert that line item total = 
        # quantity * (artwork_price + frame_price)
        self.assertEqual(line_item.line_item_total,
                         line_item.quantity * (artwork.price + frame.price))
        # check that the order total is updated to quantity * line item total
        self.assertEqual(order.order_total,
                         line_item.quantity * line_item.line_item_total)
