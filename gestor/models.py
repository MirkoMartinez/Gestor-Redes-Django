from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100) # ej: "Vibra Alto" o "El Próspero SRL"
    rubro = models.CharField(max_length=100, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    ESTADOS = [
        ('Borrador', 'Borrador'),
        ('Aprobado', 'Aprobado'),
        ('Programado', 'Programado'),
        ('Publicado', 'Publicado'),
    ]

    # Vinculamos la publicación con un cliente específico
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    red_social = models.CharField(max_length=50) # ej: Instagram, LinkedIn
    fecha_publicacion = models.DateTimeField()
    texto_posteo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Borrador')

    def __str__(self):
        return f"{self.cliente.nombre} - {self.red_social} ({self.fecha_publicacion.date()})"
# Create your models here.
