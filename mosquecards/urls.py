from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:mosque_id>', views.mosquedetails, name='mosquedetails'),
    path('mosquedetails', views.addmosquedetails, name='addmosquedetails'),
    path('addnewmosque', views.addmosque , name='addmosque'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('search', views.search, name='search'),










]
