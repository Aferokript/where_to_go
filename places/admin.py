from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


class ImagePreviewMixin:
    def image_preview(self, obj):
        if not obj.image:
            return '—'
        return format_html('<img src="{}" height="200" />', obj.image.url)


class ImageStackInline(ImagePreviewMixin, SortableStackedInline):
    model = Image
    readonly_fields = ('image_preview',)
 
    
@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        ImageStackInline
    ]
    

@admin.register(Image)
class ImageAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('place', 'image_preview')
