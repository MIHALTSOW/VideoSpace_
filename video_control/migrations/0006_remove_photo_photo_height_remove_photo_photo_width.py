# Generated by Django 5.1.1 on 2024-10-25 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_control', '0005_photo_resized_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='photo_height',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo_width',
        ),
    ]
