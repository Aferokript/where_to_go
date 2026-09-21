from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = HTMLField()
    description_short = HTMLField()
    description_long = HTMLField()
    lon = models.FloatField()
    lat = models.FloatField()
    
    place_for_order = models.PositiveIntegerField(
        default = 0,
        blank = True,
        null = True
    )
    
    class Meta:
        ordering = ['place_for_order']
        
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    
    image_for_order = models.PositiveIntegerField(
        blank = True,
        null = True
    )
    
    
    class Meta():
        ordering = ['image_for_order']
    
    
    def __str__(self):
        return f'{self.place} {self.image}'
    
    


    
