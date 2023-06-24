from django.shortcuts import render
import folium
from .models import Location
from folium.plugins import FastMarkerCluster


from django.shortcuts import render
import folium
from .models import Location
from folium.plugins import MarkerCluster


from django.shortcuts import render
import folium
from .models import Location
from folium.plugins import MarkerCluster


from django.shortcuts import render
import folium
from .models import Location
from folium.plugins import MarkerCluster


def home(request):
    locations = Location.objects.all()

    initialMap = folium.Map(location=[40.8218488, 73.581502], zoom_start=7)
    marker_cluster = MarkerCluster().add_to(initialMap)

    for location in locations:
        coordinates = (location.lat, location.lng)
        popup_content = f"<strong><span style='font-size: 14px;'>Наименование:</span></strong> {location.name}"
        icon = folium.Icon(icon='hospital', prefix='fa', color='red')
        folium.Marker(coordinates, popup=popup_content, icon=icon).add_to(marker_cluster)

    context = {'map': initialMap._repr_html_(), 'locations': locations}
    return render(request, 'map/home.html', context)


