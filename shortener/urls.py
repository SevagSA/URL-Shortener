from django.urls import path
from .views import home, go

app_name = 'shortener'
urlpatterns = [
    path('', home, name='home'),
    path('go/', go, name='go'),
]
