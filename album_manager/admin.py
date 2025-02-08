from django.contrib import admin
from .models import Album, Artista

# Register your models here.
@admin.register(Album)
class AlbumAdmin (admin.ModelAdmin):
        pass

@admin.register(Artista)
class ArtistaAdmin (admin.ModelAdmin):
        pass