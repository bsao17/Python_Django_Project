from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def djangorocks(request):
    return HttpResponse('This is a jazzy response')

def picture_details(request, category, year=0, month=0, day=0):
    template = loader.get_template('appTwo/index.html')
    context = {
        'title':'Here is the Pictures Details !',
        'category': category,
        'year': year,
        'month': month,
        'day': day

    }
    return HttpResponse(template.render(context, request))

