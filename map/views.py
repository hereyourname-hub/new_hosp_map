from django.shortcuts import render
import folium
from .models import Location
from folium.plugins import FastMarkerCluster


def home(request):
    locations = Location.objects.all()

    initialMap = folium.Map(location=[40.8218488, 73.581502], zoom_start=7)

    latitudes = []
    longitudes = []
    for location in locations:
        lat = location.lat
        latitudes.append(lat)

    for location in locations:
        lng = location.lng
        longitudes.append(lng)

    print(latitudes)
    print(longitudes)
    print(list(zip(latitudes, longitudes)))

    FastMarkerCluster(data=zip(latitudes, longitudes)).add_to(initialMap)

    # for location in locations:
    #     coordinates = (location.lat, location.lng)
    #     folium.Marker(coordinates, popup='Наименование: ' + location.name).add_to(initialMap)

    context = {'map': initialMap._repr_html_(), 'locations': locations}
    return render(request, 'map/home.html', context)
