from django.contrib import admin
from django.utils.safestring import mark_safe

from cms.models import CmsSlider

class CmsAdmin(admin.ModelAdmin):
    list_display = ('slide_title', 'slide_text', 'slide_css', 'get_image',)
    list_display_links = ('slide_title',)
    list_editable = ('slide_css',)
    fields = ('slide_title', 'slide_text', 'slide_css', 'slide_img', 'get_image',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.slide_img:
            return mark_safe(f'<img src="{obj.slide_img.url}" width="88px">')
        else:
            return 'нет картинки'

    get_image.short_description = 'Миниатюра'
# Register your models here.
admin.site.register(CmsSlider, CmsAdmin)