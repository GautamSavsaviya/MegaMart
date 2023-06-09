from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='mega-mart-home'),
    path('about/', views.about, name='mega-mart-about'),
    path('contact/', views.contact, name='mega-mart-contact'),
    path('search/', views.search, name='mega-mart-search'),
    path('product-detail/', views.product_detail, name='mega-mart-product-detail'),
]
