# Generated by Django 2.0 on 2017-12-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_artist_related_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
