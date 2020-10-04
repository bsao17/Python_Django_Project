from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a jazzy response')

def picture_details(request, category, year=0, month=0, day=0):
    template = loader.get_template('appTwo/index.html')
    return HttpResponse(template.render({}, request))

