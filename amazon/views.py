from django.shortcuts import render, get_object_or_404
from amazon import Amazon
from django.http import HttpResponse
from lists.models import List
import json
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def get_asin(request):
    output = {}
    if request.method == "GET":
        if request.GET.get("url"):
            amazon      = Amazon()
            url = request.GET.get("url")
            asin        = amazon.get_asin_from_url(url)
            output["asin"] = asin
            return HttpResponse(json.dumps(output), content_type="application/json")

@csrf_exempt
def get_item_for_asin(request, asin):
    output = {}
    if request.method == "GET":
        amazon                  = Amazon()
        item                    = amazon.get_item_by_asin(asin)
        output["asin"]          = str(asin)
        output["url"]           = str(item.Items.Item.DetailPageURL)
        output["manufacturer"]  = str(item.Items.Item.ItemAttributes.Manufacturer)
        output["product_group"] = str(item.Items.Item.ItemAttributes.ProductGroup)
        output["title"]         = str(item.Items.Item.ItemAttributes.Title)
        output["description"]   = str(item.Items.Item.ItemLinks.ItemLink.Description)
        output["short_url"]     = "http://amzn.com/%s" % asin

        return HttpResponse(json.dumps(output), content_type="application/json")
