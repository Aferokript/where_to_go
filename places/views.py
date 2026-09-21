from django.shortcuts import render
from .models import Place
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
import json


def index(request):
    features = []

    for place in Place.objects.all():
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place_detail", args=[place.id])
            },
        })

    place_data = {
        "type": "FeatureCollection",
        "features": features,
    }

    context = {"place_data": json.dumps(place_data, ensure_ascii=False)}
    return render(request, 'index.html', context)


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lon,
        },
    }
    context = {'place_data': place_data}
    return JsonResponse(place_data, json_dumps_params={'ensure_ascii': False})
      
    



    
