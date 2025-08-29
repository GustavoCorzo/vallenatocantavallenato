from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from PIL import Image
import uuid

class Role(models.Model): 
    COMPOSITOR = 'compositor' 
    ACORDEONERO = 'acordeonero' 
    CANTANTE = 'cantante'
    CORISTA = 'corista'
    CAJERO = 'cajero'
    GUACHARAQUERO = 'guacharaquero'
    GUITARRISTA = 'guitarrista'
    
    ROLE_CHOICES = [ 
        (COMPOSITOR, 'Compositor'), 
        (ACORDEONERO, 'Acordeonero'), 
        (CANTANTE, 'Cantante'), 
        (CORISTA, 'Corista'),
        (CAJERO, 'Cajero'),
        (GUACHARAQUERO, 'Guacharaquero'),
        (GUITARRISTA, 'Guitarrista'),
    ]

    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Persona(models.Model):
    NINGUNO = "0"
    PRIMARIA = "1"
    SECUNDARIA = "2"
    PREGRADO = "3"
    POSGRADO = "4"
    FORMACION_ACADEMICA_CHOICES = [
        (NINGUNO, "Ninguno"),
        (PRIMARIA, "Primaria"),
        (SECUNDARIA, "Secundaria"),
        (PREGRADO, "Pregrado"),
        (POSGRADO, "Posgrado"),
    ]

    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    formacion_academica = models.CharField(
        max_length=1,
        choices=FORMACION_ACADEMICA_CHOICES,
        default=PRIMARIA,
    )
    
    nombre_artistico = models.CharField(max_length=100)
    anio_nace = models.IntegerField(null=True, blank=True)
    lugar_nace = models.CharField(max_length=50, null=True, blank=True)
    lugar_muere = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    roles = models.ManyToManyField(Role, blank=True)
   
    class Meta:
        ordering = ["apellidos"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen and hasattr(self.imagen, 'path'):
            img = Image.open(self.imagen.path)
            max_size = (200, 200)
            img.thumbnail(max_size, Image.LANCZOS)
            img.save(self.imagen.path)

    def get_formacion_academica_display(self):
        return dict(self.FORMACION_ACADEMICA_CHOICES).get(self.formacion_academica, "Desconocido")

    def __str__(self):
        return self.nombre_artistico  


class RitmoVallenato(models.Model):
    nombre = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.nombre
    
class CantoVallenato(models.Model):
    """Modelo que representa un canto vallenato (pero no una versión específica de ese canto)"""

    titulo = models.CharField(max_length=100)
    compositor = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True)
    #Se usa ForeignKey porque un canto normalmente tiene un sólo compositor, pero un compositor puede tener múltiĺes cantos
    ritmo = models.ForeignKey('RitmoVallenato', on_delete=models.CASCADE, null=True)

    class Meta: ordering = ["titulo"]

    def __str__(self):
        
        return f"{self.titulo} {self.compositor} {self.ritmo}"
    
    def get_absolute_url(self):        
        return reverse('canto-detalle', kwargs={'pk': self.pk})
    
class AgrupacionMusical(models.Model):
    razon_social = models.CharField(max_length=150)
    acordeonero = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_acordeonero')
    voz_principal = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_voz_principal')
    corista_uno = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True, related_name='agrupaciones_corista_uno')
    corista_dos = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True, related_name='agrupaciones_corista_dos')
    cajero = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_cajero')
    guacharaquero = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_guacharaquero')
    guitarrista = models.ForeignKey('Persona', on_delete=models.CASCADE, null=True, blank=True,related_name='agrupaciones_guitarrista')

    def __str__(self):
        return f'{self.razon_social}'
    
class AlbumVallenato(models.Model):
    cancion = models.ForeignKey('CantoVallenato', on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=100)
    agrupacion = models.ForeignKey('AgrupacionMusical', on_delete=models.SET_NULL, null=True)
    anio_graba = models.CharField(max_length=4, null=True, blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, null=True, blank=True)

    class Meta: ordering = ["anio_graba"]

    def __str__(self):
        return f'{self.cancion}, {self.titulo}, {self.agrupacion}'   

class VersionVallenato(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cancion = models.ForeignKey('CantoVallenato', on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey('AlbumVallenato', on_delete=models.SET_NULL, null=True)
    interprete = models.ForeignKey('AgrupacionMusical', on_delete=models.SET_NULL, null=True)
    def __str__(self):

        return f'{self.cancion.titulo}, {self.album.titulo}' 