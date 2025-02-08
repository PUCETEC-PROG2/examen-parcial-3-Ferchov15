from django.db import models

# Create your models here.
class Artista (models.Model):
    id_artista = models.AutoField(primary_key=True)
    nombre_artista = models.CharField(max_length=30, null=False)
    paises_origen = models.CharField(max_length=30, null=False)
     
    def __str__(self):
        return self.nombre_artista
    
class Album (models.Model):
    titulo_album = models.CharField(max_length=30, null=False)
    anio_lanzamiento = models.DateField()
    GENEROS_MUSICA = [
        ('ROCK', 'Rock'),
        ('POP', 'Pop'),
        ('RAP', 'Rap'),
        ('JAZZ', 'Jazz'),
        ('BLUES', 'Blues'),
        ('METAL', 'Metal'),
        ('CLASICA', 'Clasica'),
        ('ELECTRONICA', 'Electronica'),
        ('ELECTROSWING', 'Electroswing'),
    ]
    genero_musica = models.CharField(max_length=130, choices = GENEROS_MUSICA , null=False)
    artista_asociado = models.ForeignKey(Artista, on_delete=models.CASCADE,  null=True)
    portada = models.ImageField(upload_to="portada_images")

    def __str__(self):
        return self.titulo_album