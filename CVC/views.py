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
    data = random_style
    con = {"style":data}
    return render(req, "snack.html",context=con)
