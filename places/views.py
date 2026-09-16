from django.shortcuts import render
import json


def index(requests):
    place_data = {
          "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [37.62, 55.793676]
              },
              "properties": {
                "title": "Легенды Москвы",
                "placeId": "moscow_legends",
                "detailsUrl": "/static/places/moscow_legends.json"

              }
            },
            {
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [37.64, 55.753676]
              },
              "properties": {
                "title": "Крыши24.рф",
                "placeId": "roofs24",
                "detailsUrl": "/static/places/roofs24.json"
              }
            }
          ]
        }
        
    context = {'place_data': json.dumps(place_data, ensure_ascii=False)}
    print(">>> CONTEXT:", context['place_data'][:100])
    return render(requests, 'index.html', context)
