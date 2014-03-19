#!/bin/env python

from amazonproduct import API
from lists.models import *

class Amazon:
    def __init__(self):
        self.api             = API(locale='us'); 
        self.cart_exists     = False
        self.items = {}

    def get_items(self, list):
        items = Item.objects.filter(active=True, list=list)

        for item in items:
            self.items["%s" % item.asin] = item.quantity

    def get_cart(self):
        cart = self.api.cart_create(self.items)

        print cart.Cart.PurchaseURL
        print cart.Cart.SubTotal.FormattedPrice

        # May need this at some point?
        """
        for item in cart.Cart.CartItems:
            print dir(item.CartItem)
        """
        return cart

    def main(self):
        self.get_items()
        self.get_cart()
