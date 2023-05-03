from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", {"bands": bands})


def about(request):
    return render(request, "listings/about.html")


def phone(request):
    return render(request, "listings/contact.html")


def footer(request):
    return HttpResponse("<h1>Phone Django</h1>")
