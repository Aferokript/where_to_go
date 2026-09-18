from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


class ImageStackInline(SortableStackedInline):
    model = Image
    

@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageStackInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'place_image')
    
    
    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )

