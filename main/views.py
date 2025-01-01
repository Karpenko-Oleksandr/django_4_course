from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    content = {
        'title': 'Home - Головна',
        'content': 'Furniture store HOME'
    }
    return render(request, 'main/index.html', content)

def about(request):
    content = {
        'title': 'Home - Про нас',
        'content': 'Про нас',
        'test_on_page': "Магазин який допоможе тобі створити затишний дім."
    }
    return render(request, 'main/about.html', content)