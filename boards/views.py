from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404
import requests, xmltodict

def home(request):
    boards = 'aaa'
    return render(request, 'home.html')