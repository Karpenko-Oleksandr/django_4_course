from django.urls import path

from main import views as main_views

app_name = 'main'

urlpatterns = [
    path('', main_views.index, name='index'),
    path('about/', main_views.about, name='about'),
]

