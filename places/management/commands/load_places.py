import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('url')


    def handle(self, *args, **options):
        try:
            response = requests.get(options['url'])
            self.stdout.write('Скачиваем...')
            response.raise_for_status()
        except requests.RequestException as error:
            self.stderr.write(f'Ошибка {error}')
            return

        place_info = response.json()

        place, created = Place.objects.get_or_create(
            title=place_info.get('title'),
            short_description=place_info.get('description_short'),
            long_description=place_info.get('description_long'),
            lat=float(place_info.get('coordinates', {}).get('lat')),
            lon=float(place_info.get('coordinates', {}).get('lng')),
        )

        for index, imgs_url in enumerate(place_info.get('imgs', [])):
            filename = imgs_url.split('/')[-1]
            if Image.objects.filter(place=place, image__endswith=filename).exists():
                self.stdout.write(f'Уже есть: {filename}')
                continue
            try:
                image_response = requests.get(imgs_url)
                image_response.raise_for_status()
            except requests.RequestException as error:
                self.stderr.write(f'Ошибка {imgs_url}: {error}')
                continue

            image_data = image_response.content
            image = Image(place=place, image_order=index)
            image.image.save(
                filename,
                ContentFile(image_data),
                save=True,
            )
        return self.stderr.write('Успешно!')
            

            
            
           
                
    
        
        
            
             
         
            
            
    
