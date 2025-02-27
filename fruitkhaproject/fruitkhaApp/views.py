from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'fruitkhaApp/base.html')

def index(request):
    return render(request, 'fruitkhaApp/index.html')


def index2(request):
    return render(request, 'fruitkhaApp/index_2.html')

def about(request):
    return render(request, 'fruitkhaApp/about.html')

def cart(request):
    return render(request, 'fruitkhaApp/cart.html')

def checkout(request):
    return render(request, 'fruitkhaApp/checkout.html')

def contact(request):
    return render(request, 'fruitkhaApp/contact.html')

def singleNews(request):
    return render(request, 'fruitkhaApp/single-news.html')

def news(request):
    return render(request, 'fruitkhaApp/news.html')

def singleProduct(request):
    return render(request, 'fruitkhaApp/single-product.html')

def shop(request):
    return render(request, 'fruitkhaApp/shop.html')

