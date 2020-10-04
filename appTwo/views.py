from django.shortcuts import render
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a jazzy response')

# Create your views here.
