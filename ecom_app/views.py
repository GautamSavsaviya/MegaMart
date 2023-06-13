from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    no_slide = n//4 + ceil(n/4 - (n//4))
    params = {"product": products, "range": range(1,no_slide), "no_of_slide": no_slide}
    print(products)

    return render(request, 'ecom_app/index.html', params)


def about(request):
    return HttpResponse('MegaMart About Page')


def contact(request):
    return HttpResponse('MegaMart Contact Us Page')


def search(request):
    return HttpResponse('MegaMart Search Page')


def product_detail(request):
    return HttpResponse('MegaMart Product Detail Page')
