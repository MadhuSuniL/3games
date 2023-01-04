




from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('create/',create),
    path('search/',search),
    path('match/',match),
    path('score/',score),
    path('give_card/',give_card),
    path('on_next/',on_next_btn),
]
