from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    context = {
        "message": "coucou"
    }

    return render(request, 'website/home.html',context)


def bidule(request):


    return render(request, 'website/bidule.html',{
        "bidule":"un nouveau message"
    })