from django.shortcuts import render, get_object_or_404
from amazon import Amazon
from django.http import HttpResponse
from lists.models import List
import json

def checkout_for_list(request, list):
    lists       = get_object_or_404(List, id=list)

    output      = {}
    amazon      = Amazon()
    
    amazon.get_items(list=list)
    cart = amazon.get_cart()

    output["url"] = "%s" % (cart.Cart.PurchaseURL)
    output["subtotal"] = "%s" % (cart.Cart.SubTotal.FormattedPrice)
    print cart.Cart.PurchaseURL

    return HttpResponse(json.dumps(output), content_type="application/json")
