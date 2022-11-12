from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the GPXManager index.")

def detail(request, wpt_id):
    return HttpResponse("You're looking at question %s." % wpt_id)
