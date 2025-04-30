from django.contrib import admin
from .models import *
from .forms import *

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre","email","tipo_consulta","aviso","mensajes","fecha_enviado"]
    search_fields =["nombre","email"]
    list_filter = ["tipo_consulta","aviso"]
    list_per_page = 5  
    
admin.site.register(Contacto,ContactoAdmin)