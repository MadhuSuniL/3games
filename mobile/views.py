from django.shortcuts import render , redirect
from rest_framework.generics import RetrieveAPIView , GenericAPIView,CreateAPIView
import random 
from django.http import HttpResponse,JsonResponse
from .models import *
from rest_framework.response import Response
from .serializers import MobileSerializer
from django.views.decorators.csrf import csrf_exempt



def create(req):
    name = req.GET['name']
    count = req.GET['count']
    name = str(name).upper()
    count = int(count)
    user = SimpleUser.objects.create(name=name,total_cards=count)
    req.session['id'] = user.id
    req.session['score'] = user.total_cards
    id = user.id+18730
    name = user.name
    context = {'name':name,"id":id}
    return JsonResponse(context)


def search(req):
    id = req.GET['id']
    id2 = req.session['id']
    if int(id) != id2+18730:
        id = int(id)-18730
    id = int(id)
    user = SimpleUser.objects.get(id=id)
    name = user.name
    req.session['id2'] = user.id
    context = {'name':name}
    return JsonResponse(context)


def home(req):
    return render(req, "card-reg.html")


def match(req):
    user_id = req.session['id']
    frd_id = req.session['id2']
    user_obj = SimpleUser.objects.get(id=user_id)
    frd_obj = SimpleUser.objects.get(id=frd_id)
    cards = Mobile_cards.objects.all()
    from random import choice
    card = choice(cards)

    context = {
        "user_name":user_obj.name,
        "frd_name":frd_obj.name,
        "user_cards":user_obj.total_cards,
        "frd_cards":frd_obj.total_cards,
        'name':card.name,
        'ram':card.ram,
        'rom':card.rom,
        'camera':card.camera,
        'processor':card.processor,
        'battary':card.battary,
        'img':card.image.url
    }
    return render(req, "mobile_cards.html",context=context)



def score(req):
    user_id = req.session['id']
    frd_id = req.session['id2']
    user_obj = SimpleUser.objects.get(id=user_id)
    frd_obj = SimpleUser.objects.get(id=frd_id)
    context = {
        "user_cards":user_obj.total_cards,
        "frd_cards":frd_obj.total_cards,
        "frd_name":frd_obj.name,
        }
    return JsonResponse(context)


def give_card(req):
    user_id = req.session['id']
    frd_id = req.session['id2']
    user_obj = SimpleUser.objects.get(id=user_id)
    if user_obj.total_cards > 0:
        user_obj.total_cards-=1
        user_obj.save()
        req.session['score'] = user_obj.total_cards

    frd_obj = SimpleUser.objects.get(id=frd_id)
    frd_obj.total_cards+=1
    frd_obj.save()
        
    return JsonResponse({"msg":"done"})


def on_next_btn(req):
    score = req.session['score']
    user_id = req.session['id']
    user_obj = SimpleUser.objects.get(id=user_id)
    if score != user_obj.total_cards:
        req.session['score'] = user_obj.total_cards
        return JsonResponse({"val":"y"})
    return JsonResponse({"val":"n"})
   