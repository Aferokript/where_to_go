from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=40)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    lon = models.FloatField()
    lat = models.FloatField()
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/')
    
    
    def __str__(self):
        return f'{self.place} {self.image}'
    
    
