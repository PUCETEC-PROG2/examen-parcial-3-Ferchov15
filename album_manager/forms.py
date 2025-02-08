from django import forms
from .models import Artista, Album

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre_artista', 'paises_origen']
        labels ={
            'nombre_artista': 'Nombre Artista',
            'paises_origen': 'Pais de origen',
        }
        widgets = {
            'nombre_artista': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre artista'}),
            'paises_origen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pais de Origen'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['titulo_album', 'anio_lanzamiento', 'genero_musica', 'artista_asociado', 'portada']
        labels ={
            'titulo_album': 'Titulo Album',
            'anio_lanzamiento': 'Año lanzamiento',
            'genero_musica': 'Genero Musica',
            'artista_asociado': 'Artista Asosiado',
            'portada': 'Portada'
        }
        widgets = {
            'titulo_album': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo Album'}),
            'anio_lanzamiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Año Lanzamiento'}),
            'genero_musica': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Genero Musica'}),
            'artista_asociado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Artista Asociado'}),
        }
