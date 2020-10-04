from django.shortcuts import render
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a jazzy response')

def picture_details(request, category, year=0, month=0):
    body = "category = {}, year = {}, month = {}".format(category, year, month)
    return HttpResponse(body)

