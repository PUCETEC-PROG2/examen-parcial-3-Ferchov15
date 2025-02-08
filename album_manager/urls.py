# Ingresar tus URLs de la app aquí
from django.urls import path
from . import views

app_name = 'album_manager'
urlpatterns = [
    path("", views.index, name="index"),
    path("artistas/", views.Artistas, name="artistas"),
    path('crear_artista/', views.crear_artista, name='crear_artista'),
    path('crear_album/', views.crear_album, name='crear_album'),
    path("artistas/edit_artista/<int:id_artista>/", views.edit_artista, name="edit_artista"),
    path("artistas/delet_artista/<int:id_artista>/", views.delet_artista, name="delet_artista"),
    path("edit_album/<int:album_id>/", views.edit_album, name="edit_album"),
    path("delet_album/<int:album_id>/", views.delet_album, name="delet_album"),
    path("artistas/artista/<int:id_artista>/", views.artista, name="artista"),
    path("album/<int:album_id>/", views.album, name="album"),
]