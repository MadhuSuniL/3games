from django.shortcuts import render , redirect
from rest_framework.generics import RetrieveAPIView , GenericAPIView,CreateAPIView
import random 
from django.http import HttpResponse ,JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .extra import random_style ,check_any4

def home(req):
    return render(req, "index.html")


def snack(req):
    data_list = random_style()
    con = {"style":data_list[0],"snakes":data_list[1],'lifts':data_list[2],'dinos':data_list[3],"snakes_red":data_list[4],'lifts_red':data_list[5],'dinos_red':data_list[6],"set_lift":data_list[7],'set_snake':data_list[8],'set_dino':data_list[9]}
        
    return render(req, "snack.html",context=con)

def any4(req):
        
    return render(req, "any4.html")


def get_positions(req):
    a = req.GET['1']
    b = req.GET['2']
    data = req.GET
    res = check_any4(data)
    data = {
        'res':res  
        }
    return JsonResponse(data)
