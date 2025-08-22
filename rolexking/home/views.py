from django.shortcuts import render, HttpResponse
from home.models import Rolex_Number
# Create your views here.

def index(request):
    #load all the data
    secret=Rolex_Number.objects.all()
    print(secret)
    data={
        'secret': secret
    }
    return render(request, 'index.html', context=data)


def custom_page_not_found(request):
    return render(request, "404.html", status=404)

def about(request):
    return render(request, 'about.html')