from django.contrib import admin
from .models import Turist, Imagen

class TuristAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Apellido','telefono','pais','lugar','Opinion')
    search_fields = ['Nombre']
    list_filter = ('lugar',)

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('link','Titulos','Descripcion')
    search_fields = ['Titulos']
    list_filter = ('Titulos',)

admin.site.register(Turist, TuristAdmin)
admin.site.register(Imagen, ImagenAdmin)
