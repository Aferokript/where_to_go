from django.core.management.base import BaseCommand
from places.models import Place, Image 
from django.core.files.base import ContentFile
import requests



class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('url')
        
         
    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
                
        place_info = response.json()
                
        place, created = Place.objects.get_or_create(
            title = place_info.get('title'),
            description_short = place_info.get('description_short'),
            description_long = place_info.get('description_long'),
            lat = float(place_info.get('coordinates', {}).get('lat')),
            lon = float(place_info.get('coordinates', {}).get('lng'))
        )
        
        for imgs_url in place_info.get('imgs'):
            image_response = requests.get(imgs_url)
            image_response.raise_for_status()
            
            image_data = image_response.content
            image = Image(place=place)
            image.image.save(
                'place_image',
                ContentFile(image_data),
                save=True
            )
            
            
           
                
    
        
        
            
             
         
            
            
    