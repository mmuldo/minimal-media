from django.http import HttpResponse
from django.shortcuts import render
from .instafeed import *
import os

username = os.getenv("INSTA_USER")
password = os.getenv("INSTA_PASS")

def index(request):
    feed = getFeed(username, password)
    context = {'feed': feed}
    return render(request, 'instagram/index.html', context)
