from django.shortcuts import render , redirect
from rest_framework.generics import RetrieveAPIView , GenericAPIView,CreateAPIView
import random 
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .extra import random_style

def home(req):
    return render(req, "index.html")


def snack(req):
    data_list = random_style()
    # print(data)
    con = {"style":data_list[0],"snakes":data_list[1],'lifts':data_list[2],'dinos':data_list[3],"snakes_red":data_list[4],'lifts_red':data_list[5],'dinos_red':data_list[6],"set_lift":data_list[7],'set_snake':data_list[8],'set_dino':data_list[9]}
    
    # for i, v in con.items():
    #     print(v)
    #     print()
        
    return render(req, "snack.html",context=con)
