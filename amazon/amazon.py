#!/bin/env python

from amazonproduct import API
from lists.models import *
import re
from urlparse import urlparse

class Amazon:
    def __init__(self):
        self.api             = API(locale='us'); 
        self.cart_exists     = False
        self.items = {}

    def get_asin_from_url(self, url):
        parts = urlparse(url)
        path_parts = parts.path.split("/")

        max = len(path_parts)-1
        reg = re.compile("^([A-Za-z0-9]{10})$")
        while max >= 0:
            result = reg.match(path_parts[max])
            if result:
                return path_parts[max]
            max = max-1
        return None

    def get_item_by_asin(self, asin):
        item = self.api.item_lookup(asin)
        return item

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
