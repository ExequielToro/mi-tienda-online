from django.db import models

class ProductoMedico(models.Model):
    p_numb = models.IntegerField(null=True)
    p_nombre = models.CharField(max_length=100)
    p_descripcion = models.TextField()
    p_precio = models.IntegerField()
    p_img = models.ImageField(null=True)

    def __str__(self):
        return self.p_nombre
    
opcion_consulta = [
    [0, "Consulta"],
    [1, "Sugerencia"],
    [2, "Reclamo"],
    [3, "No deseo Responder"],
    [4, "Otro"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opcion_consulta)
    mensajes = models.TextField(max_length=500)
    aviso = models.BooleanField(verbose_name="Acepto Términos y Condiciones")
    fecha_enviado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre


