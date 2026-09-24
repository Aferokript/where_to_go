from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=120,
        blank=False,
        verbose_name='название',
    )
    short_description = models.TextField(
        blank=True,
        verbose_name='краткое описание',
    )
    long_description = HTMLField(
        blank=True,
        verbose_name='полное описание',
    )
    lon = models.FloatField(
        verbose_name='долгота',
    )
    lat = models.FloatField(
        verbose_name='широта',
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='место',
    )
    image = models.ImageField(
        upload_to='places/',
        verbose_name='фото',
    )

    image_order = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name='порядок',
        db_index=True
    )

    class Meta:
        ordering = ['image_order']
        verbose_name = 'фото'
        verbose_name_plural = 'фото'


    def __str__(self):
        return f'{self.place} {self.image}'

    
