from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_2', views.index2, name='index_2'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('single-news', views.singleNews, name='single-news'),
    path('news', views.news, name='news'),
    path('single-product', views.singleProduct, name='single-product'),
    path('shop', views.shop, name='shop'),
]