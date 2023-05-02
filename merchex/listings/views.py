from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("<h1>Hello Django</h1>.")

def about(request):
    return HttpResponse("<h1>About Django</h1>.")

def phone(request):
    return HttpResponse("<h1>Phone Django</h1>.")

def footer(request):
    return HttpResponse('<h1>Phone Django</h1>')