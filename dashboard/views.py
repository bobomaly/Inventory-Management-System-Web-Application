from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Index page')


def staff(request):
    return HttpResponse('Staff page')
