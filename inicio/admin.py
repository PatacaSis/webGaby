from django.contrib import admin
from .models import Categoria,Proyecto,Imagen,Fofografia

admin.site.site_header = 'Sitio Web de Arquitectura'
admin.site.site_title = 'Admin del sitio web'
admin.site.index_title = 'Administración de la Pag Web de Gabriel Borella'

class ProyectoAdmin(admin.ModelAdmin):
        list_display= ('orden','nombre','anio','estado')

class CategoriaAdmin(admin.ModelAdmin):
        list_display= ('id','nombre')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Imagen)
admin.site.register(Fofografia)

