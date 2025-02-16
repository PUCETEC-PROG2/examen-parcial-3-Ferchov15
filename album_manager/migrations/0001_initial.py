# Generated by Django 4.2 on 2025-02-08 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_artista', models.CharField(max_length=30)),
                ('paises_origen', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_album', models.CharField(max_length=30)),
                ('anio_lanzamiento', models.DateField()),
                ('genero_musica', models.CharField(choices=[('ELECTRONICA', 'Electronica'), ('JAZZ', 'Jazz'), ('ELECTROSWING', 'Electroswing'), ('RAP', 'Rap'), ('METAL', 'Metal'), ('CLASICA', 'Clasica'), ('BLUES', 'Blues'), ('ROCK', 'Rock'), ('POP', 'Pop')], max_length=130)),
                ('portada', models.ImageField(upload_to='portada_images')),
                ('artista_asociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album_manager.artista')),
            ],
        ),
    ]
