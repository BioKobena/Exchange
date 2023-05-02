from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(
        f""" 
    <h1>Hello World!</h1>
    <p>Mes groupes préférés sont : </p>
    <ul> 
        <li> 
         Name : {bands[0].name}
        </li> 
     <li> 
         Name : {bands[1].name}
        </li> 
         <li> 
         Name : {bands[2].name}
        </li> 
    </ul> 
    """
    )


def about(request):
    lists = Listing.objects.all()
    return HttpResponse(
        f""" 
    <h1>Hello World!</h1>
    <p>Mes titres préférés sont : </p>
    <ul> 
        <li> 
         Title : {lists[0].title}
        </li> 
     <li> 
         Title : {lists[1].title}
        </li> 
         <li> 
         Title : {lists[2].title}
        </li> 
    </ul> 
    """
    )


def phone(request):
    return HttpResponse("<h1>Phone Django</h1>.")


def footer(request):
    return HttpResponse("<h1>Phone Django</h1>")
