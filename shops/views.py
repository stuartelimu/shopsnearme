from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

latitude = 0.32358400000000004
longitude = 32.5935104

# user_location = Point(longitude, latitude, srid=4326)
user_location = fromstr("POINT" + "("+str(longitude)+" "+str(latitude)+")", srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'shops/index.html'