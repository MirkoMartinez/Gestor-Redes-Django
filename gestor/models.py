from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    rubro = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    ESTADOS = [
        ('Borrador', 'Borrador'),
        ('Programado', 'Programado'),
        ('Publicado', 'Publicado'),
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    red_social = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField()
    texto_posteo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Borrador')
    
    # El nuevo campo para fotos
    imagen = models.ImageField(upload_to='posteos/', null=True, blank=True)

    def __str__(self):
        return f"{self.red_social} - {self.cliente.nombre}"