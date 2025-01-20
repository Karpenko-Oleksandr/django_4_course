from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    content = {
        'title':'Home - Главная',
        'content':'Магазин мебели HOME',

        
    }

    return render(request, 'main/index.html', content)

def about(request):
    content = {
        'title':'HOME - О нас',
        'content':'О нас',
        'text_on_page': "Текст который отвечает почему надо выбирать наш магазин."
        
    }

    return render(request, 'main/about.html', content)