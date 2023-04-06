from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def moon(request):
    return HttpResponse('<h1>My name is Moon!</h1>')

def mamun(request):
    return HttpResponse('<marquee><h1>Moon love Mamun,Mamun love moon</h1></marquee>')
