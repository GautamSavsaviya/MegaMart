from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'ecom_app/index.html')


def about(request):
    return HttpResponse('MegaMart About Page')


def contact(request):
    return HttpResponse('MegaMart Contact Us Page')


def search(request):
    return HttpResponse('MegaMart Search Page')


def product_detail(request):
    return HttpResponse('MegaMart Product Detail Page')
