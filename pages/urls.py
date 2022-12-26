from django.urls import path
from . import views
urlpatterns = [
    #127.0.0.1:8000/pages/index
    path('index/' , views.pagesIndex , name ='pagesindex'),
    #127.0.0.1:8000/pages/about
    path('about/' , views.renderAbout , name = "pagesabout"),
    #127.0.0.1:8000/pages
    path('' , views.renderHtml , name ="pagesdefault"),
    path('cars/' , views.viewCars , name ="viewCars"),

]