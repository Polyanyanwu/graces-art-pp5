# Generated by Django 3.2 on 2022-07-30 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0004_rename_artworks_artwork'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='art_style',
            new_name='style',
        ),
    ]
