from django.http import HttpResponse
from django.shortcuts import render
from .instafeed import *
import os
import requests

username = os.getenv("INSTA_USER")
password = os.getenv("INSTA_PASS")

def index(request):
    feed = getFeed(username, password)
    context = {'feed': feed}
    return render(request, 'instagram/index.html', context)

def tcat(request):
    return HttpResponse(requests.get('https://www.instagram.com/p/BLw_qaTDHrd/'))
