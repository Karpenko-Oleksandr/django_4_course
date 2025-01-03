from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):
    categories = Categories.objects.all()

    content = {
        'title': 'Home - Головна',
        'content': 'Furniture store HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', content)

def about(request):
    content = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'test_on_page': "Магазин який допоможе тобі створити затишний дім."
    }
    return render(request, 'main/about.html', content)