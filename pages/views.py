from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
# Create your views here.
def pagesIndex(request):
    return HttpResponse("hello from pages / idex")
def pagesAbout(request):
    return HttpResponse ("hello from pages / about ")
def renderHtml(request):
    listofUsers=[{"name":"shimaa"  , "age" : 23},{"name":"mohammed"  , "age" : 25},{"name":"salma"  , "age" : 22}]
    dict = {"users" : listofUsers}
    # dict = {"user":"mohammed" , "age" : 23 , "salary" : 10000000000000000} 
    return render (request , 'pages/index.html' ,dict)
def renderAbout(request):
    return render (request , 'pages/about.html')
def viewCars(request):
    # return render(request,'pages/cars.html', {"car":Car.objects.get(id = 9)})
    #  return render(request,'pages/cars.html', {"cars":Car.objects.filter(name = "BMW")})
    return render(request,'pages/cars.html', {"cars":Car.objects.all().order_by('model').exclude(name="Lancer").filter(price__range=(10 , 40)).count})
    # return render(request,'pages/cars.html' , {"ahmed" : Car.objects.all()})

