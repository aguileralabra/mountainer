from django.contrib import admin
from .models import Turist, Imagen

class TuristAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Apellido','telefono','pais','lugar','Opinion')

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('link','titulos','descripcion')

admin.site.register(Turist, TuristAdmin)
admin.site.register(Imagen, ImagenAdmin)
