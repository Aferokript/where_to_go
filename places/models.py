from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=40)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    lon = models.FloatField()
    lat = models.FloatField()
    
    place_for_order = models.PositiveIntegerField(
        default = 0,
        blank = False,
        null = False
    )
    
    class Meta:
        ordering = ['place_for_order']
        
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    image_for_order = models.PositiveIntegerField(
        blank = False,
        null = False
    )
    
    
    class Meta():
        ordering = ['image_for_order']
    
    
    def __str__(self):
        return f'{self.place} {self.image}'
    
