from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    content = {
        'title': 'HoneyShop',
        'content': 'Main page - HoneyShop'
    }
    return render(request, 'main/index.html', content)

def about(request):
    return HttpResponse('About page')