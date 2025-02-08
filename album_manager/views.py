from django.shortcuts import render, redirect
from .models import Album, Artista
from django.http import HttpResponse
from django.template import loader
from .forms import ArtistaForm, AlbumForm

# Create your views here.
def index(request):
    albums = Album.objects.all() 
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'albums': albums}, request))

def Artistas(request):
    artistas = Artista.objects.all() 
    template = loader.get_template('artistas.html')
    return HttpResponse(template.render({'artistas': artistas}, request))

def artista(request, id_artista):
    artista = Artista.objects.get(pk = id_artista)
    template = loader.get_template('display_artista.html')
    context = {
        'artista': artista
    }
    return HttpResponse(template.render(context, request))

def album(request, album_id):
    album = Album.objects.get(pk = album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))

def crear_artista(request):
    if request.method == "POST":
        form = ArtistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artistas')  
    else:
        form = ArtistaForm()
    
    return render(request, "artista_form.html", {"form": form})

def edit_artista(request, id_artista):
    artista = Artista.objects.get(pk = id_artista)
    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('album_manager:artistas')
    else:
        form = ArtistaForm(instance=artista)

    return render(request, 'artista_form.html', {'form':form})

def delet_artista(request, id_artista):
    artista = Artista.objects.get(pk = id_artista)
    artista.delete()
    return redirect('album_manager:artistas')



# Vista para crear un álbum
def crear_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm()
    
    return render(request, "album_form.html", {"form": form})

def edit_album(request, album_id):
    album = Album.objects.get(pk = album_id)
    if request.method == "POST":
        form = ArtistaForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AlbumForm(instance=album)

    return render(request, 'album_form.html', {'form':form})

def delet_album(request, album_id):
    album = Album.objects.get(pk = album_id)
    album.delete()
    return redirect('/')
