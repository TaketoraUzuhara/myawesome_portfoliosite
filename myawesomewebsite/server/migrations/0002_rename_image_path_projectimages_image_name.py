# Generated by Django 3.2.4 on 2021-06-28 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectimages',
            old_name='image_path',
            new_name='image_name',
        ),
    ]
